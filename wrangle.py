import env
import pandas as pd
import numpy as np
import utilities as utils

def _combine_csv_files(data_path=""):
    fake_df = pd.read_csv(data_path + "Fake.csv")
    fake_df['is_fake'] = True
    
    true_df = pd.read_csv(data_path + "True.csv")
    true_df['is_fake'] = False
    
    articles_df = pd.concat([true_df, fake_df], axis=0)
    articles_df = articles_df.reset_index()
    articles_df = articles_df.drop(columns=['index'])
    
    return articles_df

def _truncate_month(string_date):
    three_letter_month = string_date[0:3]
    first_space_index = string_date.find(" ")
    day_year = string_date[first_space_index:]
    
    return three_letter_month + day_year

def _determine_value_in_correct_format(string):
    """
    Dates should be standardized to 'MMM d, yyyy' (11 chars) or 'MMM dd, yyyy' (12 chars)
    """
    return (len(string) == 11) | (len(string) == 12)

def _standardize_dates(df):
    articles_df = df.copy()
    
    articles_df.date = articles_df.date.str.strip()
    articles_df.date = articles_df.date.apply(_truncate_month)
    
    # These rows did not have any value that could be parsed to a datetime and were dropped
    articles_df = articles_df.drop(index=[30775, 36924, 36925, 37256, 37257, 38849, 38850, 40350, 43286, 43287])
    
    articles_df['correct_date_format'] = articles_df.date.apply(_determine_value_in_correct_format)
    
    # Any row that did not have a correct date format were assigned Aug 16, 2016 since it was near the middle range of dates for all observations
    for row in articles_df[articles_df.correct_date_format == False].index:
        articles_df.date[row] = "Aug 16, 2016"
    
    articles_df = articles_df.drop(columns=['correct_date_format'])
    
    return articles_df

def _nlp_clean_titles_and_text(df):
    articles_df = df.copy()
    
    articles_df['clean_title'] = articles_df.title.apply(utils.nlp_basic_clean)
    articles_df.clean_title = articles_df.clean_title.apply(utils.nlp_tokenize)
    articles_df.clean_title = articles_df.clean_title.apply(utils.nlp_remove_stopwords, extra_words=["reuters"])
    articles_df.clean_title = articles_df.clean_title.apply(utils.nlp_lemmatize)
    
    articles_df['clean_text'] = articles_df.text.apply(utils.nlp_basic_clean)
    articles_df.clean_text = articles_df.clean_text.apply(utils.nlp_tokenize)
    articles_df.clean_text = articles_df.clean_text.apply(utils.nlp_remove_stopwords, extra_words=["reuters"])
    articles_df.clean_text = articles_df.clean_text.apply(utils.nlp_lemmatize)
    
    return articles_df

def _drop_empty_rows(df):
    articles_df = df.copy()
    
    articles_df = articles_df.replace('', np.nan)
    
    return articles_df.dropna()


def wrangle_articles():
    articles_df = _combine_csv_files(env.data_path)
    
    articles_df = _standardize_dates(articles_df)
    articles_df.date = pd.to_datetime(articles_df.date, format="%b %d, %Y")
    
    articles_df = _nlp_clean_titles_and_text(articles_df)
    articles_df = articles_df.sort_values(by='date')
    
    articles_df = _drop_empty_rows(articles_df)
    articles_df = articles_df.drop_duplicates(subset=['title','text'])
    
    return articles_df