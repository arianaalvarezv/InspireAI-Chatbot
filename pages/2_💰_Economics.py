import openai
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit_chat import message

# Config
st.set_page_config(page_title='Economics - InspireAI', page_icon='💡', layout='wide')
# st.markdown("<h1 style='text-align: center;'>InspireAI - Your personal tutor ChatBot 💡</h1>", unsafe_allow_html=True)

# Set API key
openai.api_key = "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"

# Title
st.title('💰 Economics AI Tutor')