import streamlit as st
import requests
import numpy as np

st.markdown("""# Let's try a gif from GIPHY
"""
)

url = 'https://api.giphy.com/v1/gifs/search'
query = st.text_input('Search a GIF')
limit_gifs = 3

params = {'api_key': st.secrets.api_key, 'q': query, 'limit': limit_gifs, 'rating': 'g', 'lang': 'en'}
response = requests.get(url, params=params).json()

while not query:
    st.stop()

url_gif = response['data'][np.random.randint(0, limit_gifs)]['embed_url']

st.write(f'<iframe src="{url_gif}" width="480" height="240">',
         unsafe_allow_html=True
         )

st.write(st.secrets['magic'])
