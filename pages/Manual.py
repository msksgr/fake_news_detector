import streamlit as st

# Set page config
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🤖",
    # layout="wide",
    initial_sidebar_state="expanded"
)


st.title('Fake News Detector User Manual')

# Make sure to update to the latest URL
app_url = 'https://2-stepfakenewsdetector.streamlit.app/'
github_url = 'https://github.com/Jeisson-rojas/2_Steps_Fake_News_Detector' 

# Description about the application
st.header('Introduction')
'Welcome to the Fake News Detector! git init In today\'s digital age, where misinformation is rampant, it\'s essential to verify the authenticity of news sources. Our tool aims to assist you in making informed decisions by providing insights into the likelihood of news articles being fake.'
'This prototype of our fake news detector is built with the upcoming US presidential election in mind. We understand the importance of identifying fake news and avoiding misinformation, especially during crucial events like elections. Our machine learning model, based on LSTM neural networks trained with a dataset of fake and real news, provides accurate predictions of news authenticity. For more details about our model, please visit our GitHub repository.'
st.page_link(github_url, label='GitHub Repository', icon='🔗')

# Description about the manual
st.header('Accessing the application')
'To begin using the Fake News Detector:'
'* Open the application link provided below in your web browser:'
st.page_link(app_url, label='Fake News Detector', icon='🔗')
'* The application is compatible with the two most recent versions of the following browsers: Google Chrome, Mozilla Firefox, Microsoft Edge, and Safari.'   # Reference: https://docs.streamlit.io/knowledge-base/using-streamlit/supported-browsers
'* Once you\'ve accessed the application, you\'ll be presented with the main interface, where you can interact with features and functionalities.'

st.header('User Interface Overview')
'The Fake News Detector interface consists of several components:'
'* **Title and Description**: Provides an overview of the application\'s purpose and functionality.'
'* **Sidebar Navigation**: Allows you to directly access the main page and the manual.'
'* **News Selection**: Enables you to select a news article from a list to analyze its authenticity.'
'* **Result Display**: Presents the probability of the selected news being fake, along with related words and a word cloud visualization.'

st.header('Using the Application')
st.subheader('1. Selecting a News Article:')
'* Choose a news article from the dropdown list in the "Step 1: Select a news" section.'
'* The application will display the opening sentences of the selected news article.'
st.subheader('2. Analyzing the News:')
'* Click the "Submit" button to analyze the selected news article.'
'* The application will provide a probability percentage indicating the likelihood of the news being fake.'
'* Additionally, you\'ll see a gauge icon representing the probability level.'
st.subheader('3. Viewing Word Cloud:')
'* The application generates a word cloud visualization of the selected news article.' 
'* This visualization highlights the most frequent words in the news article, with word size indicating frequency.'
st.subheader('4. Exploring Related Words:')
'* After submitting, the application will display most related words in similar news articles, categorized into real and fake news groups based on the probability of the news being fake.'
'* These words are listed based on their importance in the news group.'
'* This will help you to understand the overall context of the similar news.'


'**Thank you for using the Fake News Detector! We hope this tool helps you navigate the vast landscape of online information more effectively.**'