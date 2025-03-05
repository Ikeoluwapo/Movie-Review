import nltk
import streamlit as st
import pandas as pd
nltk.download('vader_lexicon') #vader is used to analysing social media, online review etc)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from PIL import Image

st.title("THE ELLEX MOVIE REVIEW")
Movie = Image.open("THE ELLEX MOVIE.jpg")
st.image(Movie, caption = "The Ellex Movie", width = 250)
Movie2 = Image.open("THE ELLEX MIX.jpg")
st.sidebar.image(Movie2, width = 200)
st.sidebar.subheader('''This is the perfect site to give your review''')
st.sidebar.write("Kindly give your review about the Ellex Movie")


text = st.text_input("Enter your review: ")
st.spinner(text)
if text is not None:
    model = SentimentIntensityAnalyzer()
    score = model.polarity_scores(text)['compound']
    if score > 0:
        st.text("Review is positive. Thanks")
    elif score < 0:
        st.text("Negative review")
    else:
        st.text("....")

