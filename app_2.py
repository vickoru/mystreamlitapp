import streamlit as st

import numpy as np
import pandas as pd

import requests

url =  "http://localhost:8000"

st.markdown("""# This is a header for our Streamlit Demo
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

# Uploading CSV file
uploaded_csv = st.file_uploader("Choose a CSV file", type="csv", accept_multiple_files=False)
if uploaded_csv is not None:
    if st.button('Get results transfering encoded json as bytes'):
        # load the csv as dataframe
        df = pd.read_csv(uploaded_csv)
        st.write(df)
        url_endpoint = f"{url}/uploaded_csv_json" # Endpoint at app.py FastAPI script
        df_byte = df.to_json().encode()  # .to_json() converts dataframe into json object
                                     # .encode() converts json object into bytes, encoded using UTF-8
        print(df_byte) # debugging purposes
        # Transfering info in CSV file to FastAPI as an encoded json in bytes,
        # using POST method because we are sending information. The transfered
        # bytes have to be decoded as a string but in json format
        # 'myfile' name has to be used also in endpoint of FastAPI
        response = requests.post(url=url_endpoint, files={"myfile": df_byte})
        st.write(response.json()) # printing the response from app.py in FastAPI

    if st.button('Get results transfering string as bytes'):
        url_endpoint = f"{url}/uploaded_csv_string" # Endpoint at app.py FastAPI script
        # Transfering the CSV file directly to FastAPI as bytes,
        # using POST method. The CSV file is transfered in bytes and has to be
        # read as string in FastAPI
        # 'myfile' name has to be used also in endpoint of FastAPI
        response = requests.post(url=url_endpoint, files={"myfile": uploaded_csv})
        st.write(response.json()) # printing the response from app.py in FastAPI

# Uploading audio WAV file
uploaded_wav = st.file_uploader("Choose a WAV file", type="wav", accept_multiple_files=False)
if uploaded_wav:
    # read and play the audio file
    st.write('### Play audio')
    audio_bytes = uploaded_wav.read()
    st.audio(audio_bytes, format='audio/wav')

# Uploading image, only PNG AND JPG accepted
uploaded_image = st.file_uploader("Choose an image", type=["png", "jpg"], accept_multiple_files=False)
if uploaded_image:
    # read and play the audio file
    st.write('### See image')
    image_bytes = uploaded_image.read()
    st.image(image_bytes)
