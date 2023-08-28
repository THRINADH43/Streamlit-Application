import streamlit as st
import openai

import dotenv
import os

dotenv.load_dotenv() 

API_KEY = os.getenv('api_key')

# Page config
st.set_page_config(page_title='OpenAI Text Generator', page_icon=':robot:') 

# Layout
st.header('OpenAI Text Generator')

# API key
#openai.api_key = API_KEY
openai.api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Input elements
user_input = st.text_input("Enter prompt:", "")
max_tokens = st.slider("Max tokens:", 50, 1024, 100)
engine = st.selectbox("Engine:", ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"])
temperature = st.slider("Temperature:", value=0.5, min_value=0.0, max_value=1.0, step=0.1)

# Generate button
if st.button("Generate"):
    
    # Call API
    response = openai.Completion.create(
        engine=engine,
        prompt=user_input,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature
    )

    # Display response
    st.success(response.choices[0].text)

st.caption("Made with Streamlit and OpenAI API")
