import streamlit as st
import matplotlib.pyplot as plt
import spacy
from spacy.lang.el.stop_words import STOP_WORDS
from wordcloud import WordCloud
from webapp_utils import get_page_text, clean, sl
from log_model import log_model
from spacy import displacy
from spacytextblob.spacytextblob import SpacyTextBlob
from PIL import Image
import spacy_streamlit

nlp = spacy.load('en_core_web_md')
nlp.add_pipe("spacytextblob")
models = ["en_core_web_md"]
visualizers = ["ner",'tokens']


st.set_page_config(page_title = "Fake News Detector")


#@st.cache(allow_output_mutation=True)



@st.cache(suppress_st_warning=True)
def generate_output(text):
     
     text = clean(text)
     text = sl(text)
     prediction, probability = log_model(text)
    
     
     if prediction == True:
         st.markdown("<h1><span style='color:red'>❌ This is a fake news article!😡</span></h1>",
                     unsafe_allow_html=True)
     else:
         st.markdown("<h1><span style='color:green'>✅ This is a real news article!👍</span></h1>",
                     unsafe_allow_html=True)

     #q_text = '> '.join(text.splitlines(True))
     #q_text = '> ' + q_text
     doc = nlp(text)
     #st.markdown(q_text)
     
     st.write('text_polarity: ',round(doc._.polarity,2),'text_subjectivity: ',round(doc._.subjectivity,2))
     st.write('true_probability: ',round(probability[0][0],2), 'fake_probability: ',round(probability[0][1],2))
     st.markdown('-----------')
     
def cloud(text):
    font_path = 'Photos/coolvetica rg.ttf'
    wc = WordCloud(width = 1000,
                    height = 600,
                    #random_state = 1,                    
                    #stopwords = STOP_WORDS
                    max_words=None,
                    #min_font_size=,
                    font_path=font_path,
                    background_color='black',
                    mode='RGBA',
                   colormap='Greens').generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis('off')   
    st.pyplot(fig)
     
     
        
    

desc = "This web app detects fake news written in English.\
        You can either enter the URL of a news article, or paste the text here(works better)."

st.title("Fake News Detector")
image = Image.open('Photos/fofweb.jpg')
st.image(image)
st.markdown(desc)
st.subheader("Enter the URL/text of a news article written in English")
select_input = st.radio("Select Input:", ["URL", "Text"])

if select_input == "URL":
    url = st.text_input("URL")
    if st.button("Run"):
        text = get_page_text(url)
        generate_output(text)
        cloud(text)
        spacy_streamlit.visualize(models, text,visualizers=visualizers,show_visualizer_select=True)
        
        

else:
    text = st.text_area("Text", height=300)
    if st.button("Run") and len(text)>100:
        generate_output(text)
        cloud(text)
        spacy_streamlit.visualize(models, text,visualizers=visualizers,show_visualizer_select=True)
        
    else:
        st.markdown('Please enter greater than 100 characters')

st.markdown("<br><br><hr><center>Created by <a href='https://github.com/Fake-News-Capstone/fake_news_capstone#top'><strong>Codeup - Easley Cohort  2021</strong></a></center><hr>", unsafe_allow_html=True)

