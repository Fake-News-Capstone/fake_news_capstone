#-----------------------------------------------------------------------------------------------------------------

import re
import nltk
import pandas as pd
import unicodedata
import env
import utilities
import numpy as np
from PIL import Image
from wordcloud import WordCloud

#-----------------------------------------------------------------------------------------------------------------

def _show_counts_and_ratios(df, column):
    """
    This fucntion takes in a df and column name.
    Will produce a valuecounts for each label and the percetage of the
    data it represents
    """
    fof = pd.concat([df.is_fake.value_counts(),
                        df.is_fake.value_counts(normalize=True)], axis=1)
    fof.columns = ['n', 'percent']
    
    return fof

#-----------------------------------------------------------------------------------------------------------------

def _generate_list_for_clean_text(df):
    """
    This function takes in a dataframe. Produces a list of clean text that
    is seperated by white space. 
    """
    all_clean_text = " ".join(df.clean_text)
        
    return re.sub(r"[^\w\s]", "", all_clean_text).split()

#-----------------------------------------------------------------------------------------------------------------

def _percentFakevsReal(word_counts):
    """
    This function takes in word_counts and returns a horizontal bar plot of the proportions
    of Fake vs Real news for the 20 most common words
    """
    (word_counts
     .assign(p_fake=word_counts.fake / word_counts['all'],
             p_real=word_counts.real / word_counts['all'])
     .sort_values(by='all')
     [['p_fake', 'p_real']]
     .tail(20)
     .sort_values('p_real')
     .plot.barh(stacked=True))

    plt.title('Proportion of Fake vs Real news for the 20 most common words')
    
#-----------------------------------------------------------------------------------------------------------------    
    
def _wordcounts_all(word_counts):
    """
    This function takes in word_counts. Makes sure all words for 'fake' and 'all' are greater
    than 10. Generates a ratio column of fake words to all words and returns a dataframe of
    all the word counts and ratios for all, fake, and real words
    """
    word_counts_all = (word_counts
     [(word_counts.fake > 10) & (word_counts['all'] > 10)]
     .assign(ratio=lambda df: df.fake / (df['all'] + .01))
     .sort_values(by='all', ascending = False)
     .pipe(lambda df: pd.concat([df.head(), df.head(20)])))
    
    return  word_counts_all

#-----------------------------------------------------------------------------------------------------------------

def _wordcount_fake(word_counts):
    """
    This function takes in word_counts. Makes sure all words for 'fake' and 'real' are
    greater than 10. Generates a ratio column of fake words to real words and returns a
    dataframe of all the word counts and ratios for all, fake, and real words
    """
    word_counts_fake = (word_counts
     [(word_counts.fake > 10) & (word_counts.real > 10)]
     .assign(ratio=lambda df: df.fake / (df.real + .01))
     .sort_values(by='ratio', ascending = False)
     .pipe(lambda df: pd.concat([df.head(), df.head(20)])))
    
    return word_counts_fake

#-----------------------------------------------------------------------------------------------------------------

def _wordcount_real(word_counts):
    """
    This function takes in word_counts. Makes sure all words for 'fake' and 'real' are
    greater than 10. Generates a ratio column of real words to fake words and returns a
    dataframe of all the word counts and ratios for all, fake, and real words
    """
    word_counts_real = (word_counts
     [(word_counts.fake > 10) & (word_counts.real > 10)]
     .assign(ratio=lambda df: df.real / (df.fake + .01))
     .sort_values(by='ratio', ascending = False)
     .pipe(lambda df: pd.concat([df.head(), df.head(20)])))
    
    return word_counts_real

#-----------------------------------------------------------------------------------------------------------------

def _word_clouds_rfa(all_words, fake_words, real_words):
    """
    This function takes in all_words, fake_words, real_words. generates a word cloud for each
    aurgument with a fig size of (10, 8) and titles of all_cloud, fake_cloud, real_cloud.
    Returns a set of word clouds for all_words, fake_words, real_words
    """
    all_cloud = WordCloud(background_color='black', height=1000, width=400, colormap="seismic_r").generate(' '.join(all_words))
    fake_cloud = WordCloud(background_color='black', height=600, width=800, colormap="seismic_r").generate(' '.join(fake_words))
    real_cloud = WordCloud(background_color='black', height=600, width=800, colormap="seismic_r").generate(' '.join(real_words))

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.5, .5, .5, .5]), plt.axes([.5, 0, .5, .5])]

    axs[0].imshow(all_cloud)
    axs[1].imshow(fake_cloud)
    axs[2].imshow(real_cloud)

    axs[0].set_title('All Words')
    axs[1].set_title('Fake')
    axs[2].set_title('Real')

    for ax in axs: ax.axis('off')
        
    return _word_clouds_rfa

#-----------------------------------------------------------------------------------------------------------------

def _fake_bigrams(fake_words):
    """
    This function takes in fake_words. Generates a horizonalt bar chart with x and y labels
    for the top 20 fake bigrams.
    """
    top_20_fake_bigrams = (pd.Series(nltk.ngrams(fake_words, 2))
                          .value_counts()
                          .head(20))

    top_20_fake_bigrams.sort_values().plot.barh(color='blue', width=.9, figsize=(10, 6))

    plt.title('20 Most frequently occuring fake bigrams')
    plt.ylabel('Bigram')
    plt.xlabel('# Occurances')

    # make the labels pretty
    ticks, _ = plt.yticks()
    labels = top_20_fake_bigrams.reset_index()['index'].apply(lambda t: t[0] + ' ' + t[1])
    _ = plt.yticks(ticks, labels)
    
#-----------------------------------------------------------------------------------------------------------------
    
def _real_bigrams(real_words): 
    """
    This function takes in real_words. Generates a horizontal bar chart with x and y labels
    for the top 20 real bigrams.
    """
    top_20_real_bigrams = (pd.Series(nltk.ngrams(real_words, 2))
                          .value_counts()
                          .head(20))

    top_20_real_bigrams.sort_values().plot.barh(color='green', width=.9, figsize=(10, 6))

    plt.title('20 Most frequently occuring real bigrams')
    plt.ylabel('Bigram')
    plt.xlabel('# Occurances')

    # make the labels pretty
    ticks, _ = plt.yticks()
    labels = top_20_real_bigrams.reset_index()['index'].apply(lambda t: t[0] + ' ' + t[1])
    _ = plt.yticks(ticks, labels)
    
#-----------------------------------------------------------------------------------------------------------------   

def _real_trigrams(real_words):
    """
    This function takes in real_words. Generates a horizontal bar chart with x and y labels
    for the top 20 real trigrams.
    """
    top_20_real_trigrams2 = (pd.Series(nltk.ngrams(real_words, 3))
                          .value_counts()
                          .head(20))

    top_20_real_trigrams2.head()

    top_20_real_trigrams2.sort_values().plot.barh(color='blue', width=.9, figsize=(10, 6))

    plt.title('20 Most frequently occuring real Trigrams')
    plt.ylabel('Trigram')
    plt.xlabel('# Occurances')

    # make the labels pretty
    ticks, _ = plt.yticks()
    labels = top_20_real_trigrams2.reset_index()['index'].apply(lambda t: t[0] + ' ' + t[1] + ' ' + t[2])
    _ = plt.yticks(ticks, labels)
    
#-----------------------------------------------------------------------------------------------------------------    
    
def _fake_trigrams(fake_words):
    """
    This function takes in fake_words. Generates a horizontal bar chart with x and y labels
    for the top 20 fake trigrams.
    """
    top_20_fake_trigrams2 = (pd.Series(nltk.ngrams(fake_words, 3))
                          .value_counts()
                          .head(20))

    top_20_fake_trigrams2.head()

    top_20_fake_trigrams2.sort_values().plot.barh(color='green', width=.9, figsize=(10, 6))

    plt.title('20 Most frequently occuring fake Trigrams')
    plt.ylabel('Trigram')
    plt.xlabel('# Occurances')

    # make the labels pretty
    ticks, _ = plt.yticks()
    labels = top_20_fake_trigrams2.reset_index()['index'].apply(lambda t: t[0] + ' ' + t[1] + ' ' + t[2])
    _ = plt.yticks(ticks, labels)
    
#-----------------------------------------------------------------------------------------------------------------
