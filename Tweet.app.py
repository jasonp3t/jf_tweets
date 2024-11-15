import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Title of the Streamlit App
st.title('Airline Sentiment Analysis')

# Load the dataset
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/jasonp3t/jf_tweets/refs/heads/main/Tweets.csv'
    tweets = pd.read_csv(url)
    return tweets

tweets = load_data()

# Show the first few rows of the dataframe
st.subheader('Sample Tweets Data')
st.write(tweets.head())

# Display the value counts for airline sentiment
st.subheader('Airline Sentiment Distribution')
sentiment_counts = tweets['airline_sentiment'].value_counts()
st.write(sentiment_counts)

# Create a bar chart for airline sentiment
st.subheader('Airline Sentiment Bar Chart')
fig_bar = px.bar(
    x=sentiment_counts.index,
    y=sentiment_counts.values,
    labels={'x': 'Sentiment', 'y': 'Count'},
    title='Sentiment Distribution by Airline'
)
st.plotly_chart(fig_bar)

# Create a pie chart for airline sentiment using Plotly
st.subheader('Airline Sentiment Pie Chart')
fig_pie = px.pie(
    tweets,
    names=tweets['airline_sentiment'].value_counts().index,
    values=tweets['airline_sentiment'].value_counts().values,
    title='Sentiment Distribution (Pie Chart)'
)
st.plotly_chart(fig_pie)

# Create a bar chart showing tweets by airline
st.subheader('Tweets by Airline')
airline_counts = tweets['airline'].value_counts()
fig_airline = px.bar(
    x=airline_counts.index,
    y=airline_counts.values,
    labels={'x': 'Airline', 'y': 'Tweet Count'},
    title='Tweets by Airline'
)
st.plotly_chart(fig_airline)
