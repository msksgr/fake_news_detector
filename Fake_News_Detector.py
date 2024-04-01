# Import libraries
import streamlit as st
from PIL import Image
import pandas as pd
import base64

# Set page config
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# URLs for the app and GitHub repository
app_url = 'https://2-stepfakenewsdetector.streamlit.app/'
github_url = 'https://github.com/Jeisson-rojas/2_Steps_Fake_News_Detector' 

# Set background image
## Function to get image files as base64 (binary data)
@st.cache_data
def get_img_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

## Get image files as base64 (binary data) to display in the app
img_bg = get_img_as_base64("data/background.png")
img_sidebar = get_img_as_base64("data/image.jpg")

## Settings for the background image using CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img_bg}");
background-size: 100%;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

## CSS code for the background image (optional, needs to be in the above css code)
# background-position: top left;
# background-repeat: no-repeat;
# background-attachment: local;

## Sidebar photo settings (optional, needs to be in the above css code)
# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img_sidebar}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

## Display the background image
st.write(page_bg_img, unsafe_allow_html=True)


# Load news data
## News data
df_news = pd.read_excel('data/news_poc.xlsx')

## Define a function to extract opening sentences from news text
def extract_first_few_words(text, num_words):
    words = text.split()
    first_few_words = ' '.join(words[:num_words])
    return first_few_words

## Extract opening sentences from news articles
num_words = 30 # Number of words to extract
df_news['Opening'] = df_news['Text'].apply(lambda x: extract_first_few_words(x, num_words))

## Close words in the similar news
pr_excel = pd.read_excel('data/pagerank.xlsx', sheet_name=None)
df_pr_real_news_1 = pr_excel['real_news_1']
df_pr_real_news_2 = pr_excel['real_news_2']
df_pr_fake_news_1 = pr_excel['fake_news_1']
df_pr_fake_news_2 = pr_excel['fake_news_2']

# Load images
## Gauge icons for the probability of the news being fake 
img_pt1 = Image.open('data/pt1.png')
img_pt2 = Image.open('data/pt2.png')
img_pt3 = Image.open('data/pt3.png')
img_pt4 = Image.open('data/pt4.png')

## Word cloud images for each news
img_wc_real_news_1 = Image.open('data/wc_real_news_1.jpg')
img_wc_real_news_2 = Image.open('data/wc_real_news_2.jpg')
img_wc_fake_news_1 = Image.open('data/wc_fake_news_1.jpg')
img_wc_fake_news_2 = Image.open('data/wc_fake_news_2.jpg')



# Main page

# Title and description
st.title('Fake News Detector')
st.header('Welcome to our fake news detector!')

st.container()
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(
        'Not sure if a news article is real or fake? Our tool helps you determine the likelihood of news being fake.'
        )
    'This application is designed to help you distinguish between real and fake news articles. In today\'s digital age, where misinformation is rampant, it\'s essential to verify the authenticity of news sources. Our tool aims to assist you in making informed decisions by providing insights into the likelihood of news articles being fake.'
    'This prototype of our fake news detector is built with the upcoming US presidential election in mind. We understand the importance of identifying fake news and avoiding misinformation, especially during crucial events like elections.'
    'For detailed instructions on using the application, you can access the manual below or from the sidebar navigation.'
    st.page_link('pages/Manual.py', label='Manual', icon='📖')
 
    st.divider()

    # Step 1: Select a news
    st.header("Step 1: Select a News Article")
    'Choose a news article title to analyze its likelihood of being fake.'

    # Select a news title
    selected_title = st.selectbox('Select a news title:', df_news['Title'], label_visibility='collapsed')

    # Retrieve selected news data
    selected_news = df_news[df_news['Title'] == selected_title].iloc[0]
    opening_text = selected_news['Opening']
    news_num = selected_news['No.']
    probability = selected_news['Fake Probability'] * 100

    # Display the selected news
    if not selected_news.empty:  
        'You selected the news beginning with:'
        container = st.container(border=True)
        container.write(opening_text + '...')
    else:
        container = st.container(border=True)
        container.write('No news selected.')
    
    'Click the button below to analyze the news article.'

    # After submitted, show every data related to the selected news
    if st.button('Submit'):
        
        # Step 2: Display the result
        st.header('Step 2: Check the Result')

        col1, col2 = st.columns([1, 2])

        with col1:
            'The news is'
            st.subheader(f'{probability:.2f}%')
            'likely to be fake.'

        with col2:      
            # Gauge icon depending on the probability
            if probability < 25:
                st.image(img_pt1, width=250)
            elif probability < 50:
                st.image(img_pt2, width=250)
            elif probability < 75:
                st.image(img_pt3, width=250)
            else:
                st.image(img_pt4, width=250)

        # Step 3: Display word cloud
        st.header('Step 3: Word Cloud of the Selected News')
        'The word cloud shows the most frequent words in the selected news article. The size of the word indicates the frequency.'
        st.image(eval(f'img_wc_{news_num}'), width=600)

        # Step 4: Display related words
        st.header('Step 4: Related words in similar news')
        'Reviewing related words in similar news articles can help understand their context. News articles are categorized into two groups: real and fake, based on the probability of being fake.'
        'The table below shows the most related words in each news group, along with their importance.'

        st.dataframe(eval(f'df_pr_{news_num}'), hide_index=True)

        # Closing words
        'Thank you for using our Fake News Detector! We hope you find this tool helpful.'
        'For more details about the model, visit our GitHub page:'
        st.page_link(github_url, label='GitHub Repository', icon='🔗')
