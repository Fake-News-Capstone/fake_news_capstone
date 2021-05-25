import pandas as pd
import requests
from bs4 import BeautifulSoup
import utilities as utils

def get_page_text(url):
    html_page = requests.get(url).content
    soup = BeautifulSoup(html_page, 'lxml')

    whitelist = ['p', 'strong', 'em', 'b', 'u', 'i', 'h1', 'h2', 'h3']
    out = ""

    for t in soup.find_all(text=True):
        if t.parent.name in whitelist:
            out += '{} '.format(t)

    escape = ['\r', '\n', '\t', '\xa0']

    for e in escape:
        out = out.replace(e, '')

    return out

def clean(text):
    clean_text = utils.nlp_basic_clean(text)
    clean_text = utils.nlp_tokenize(clean_text)
    return clean_text
    
def sl(text):
    sl = utils.nlp_remove_stopwords(text, extra_words=["reuters"])
    sl = utils.nlp_lemmatize(sl)
    return sl

