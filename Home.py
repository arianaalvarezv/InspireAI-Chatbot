from collections import namedtuple
# import altair as alt
# import math
# import pandas as pd
import streamlit as st
# import streamlit_extras
# from streamlit_extras.switch_page_button import switch_page

#confit
st.set_page_config(
    page_title = "InspireAI", 
    page_icon="💡",
)
st.markdown("<h1 style='text-align: center;'>InspireAI - Your personal tutor ChatBot 💡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose the expertise you are looking for to maximize your learning.</h1>", unsafe_allow_html=True)


#Title
# st.title('InspireAI')

#Side Bar
st.sidebar.success("Select an AI Tutor")

#Content
# st.write(
#     """
#     Choose the expertise you are looking for.
#     """
# )

c1, c2, c3, c4 = st.columns(4)
with c1:
    # st.info("**Writing AI Tutor <a href='Writing' target='1_📝_Writing'>Writing AI Tutor</a>**", icon="📝")
    # writing = st.button("Writing AI Tutor")
    st.info('**[Writing AI Tutor](http://localhost:8501/Writing)**')
    # st.markdown("<a href='Writing' target='1_📝_Writing'>Writing AI Tutor</a>", unsafe_allow_html=True)

with c2:
    # st.markdown("<a href='Economics' target='2_💰_Economics'>Economics AI Tutor</a>", unsafe_allow_html=True)
    st.info('**[Economics AI Tutor](http://localhost:8501/Economics)**')
with c3:
    # st.markdown("<a href='Finance' target='3_📈_Finance'>Finance AI Tutor</a>", unsafe_allow_html=True)
    st.info('**[Finance AI Tutor](http://localhost:8501/Finance)**')

with c4:
    # st.markdown("<a href='Computer_Science' target='4_💻_Computer_Science'>Computer Science AI Tutor</a>", unsafe_allow_html=True)
    st.info('**[Computer Science AI Tutor](http://localhost:8501/Computer_Science)**')




