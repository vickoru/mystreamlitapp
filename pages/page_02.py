import streamlit as st
import requests
import pandas as pd

st.set_page_config(
   page_title="Streamlit demo to exchange files",
   page_icon= 'X',
   layout="wide",
   initial_sidebar_state="expanded",
)

# Main Text on Homepage
'''
# User Interface for our Streamlit Demo

'''
# File uploading section
# st.set_option('deprecation.showfileUploaderEncoding', False)

# selection = opti

url = "http://localhost:8000"


uploaded_wav = st.file_uploader("Choose a WAV file", type="wav", accept_multiple_files=False)
if uploaded_wav:
    # read and play the audio file
    st.write('### Play audio')
    audio_bytes = uploaded_wav.read()
    st.audio(audio_bytes, format='audio/wav')

uploaded_image = st.file_uploader("Choose an image", type=["png", "jpg"], accept_multiple_files=False)
if uploaded_image:
    # read and play the audio file
    st.write('### See image')
    image_bytes = uploaded_image.read()
    st.image(image_bytes)

uploaded_csv = st.file_uploader("Choose a CSV file", type="csv", accept_multiple_files=False)
if uploaded_csv is not None:
    # load the csv as dataframe
    # url_ = f'{url}/uploaded_csv'
    # url_ = "http://localhost:8000/uploaded_csv"
    print(url_)
    df = pd.read_csv(uploaded_csv)
    st.write(df)
    response = requests.post(url=url_, files={"file": uploaded_csv})
    # response = requests.get("http://localhost:8000/")
    print(response)
    # st.write(response.json()['status'])
    # response = requests.post(url_, files={"file": uploaded_csv})
    # print(response)
    # print(response.json())

# if uploaded_wav is not None:
#     # read and play the audio file
#     st.write('### Play audio')
#     audio_bytes = uploaded_wav.read()
#     st.audio(audio_bytes, format='audio/wav')

# if uploaded_image is not None:
