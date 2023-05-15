from fastapi import FastAPI, File, UploadFile

import requests
import pandas as pd
from io import StringIO, BytesIO
import json

app = FastAPI()

@app.get('/')
def index():
    return {"status": "ok"}

@app.post('/uploaded_csv_json')
def upload_file(myfile: UploadFile = File(...)):
    contents = myfile.file.read() # Reading content of 'myfile' in bytes
    # print(contents)
    decoded_str = contents.decode('utf-8') # Decoding contents into str type
    # decoded_str = StringIO(contents.decode('utf-8')) # Alternative using StringIO
    df_json = json.loads(decoded_str) # Reading string and converting to json (dictionary)
    df = pd.DataFrame(df_json) # Reading dictionary and converting into dataframe
    results = {
        'mean1': df['TotSyst_MBD'].mean(),
        'mean2': df['TotSurf_MBD'].mean()
        }
    return results

@app.post('/uploaded_csv_string')
def upload_file(myfile: UploadFile = File(...)):
    contents = myfile.file.read()
    # decoded = StringIO(contents.decode('utf-8')) # Alternative using StringIO
    # decoded_str = buffer.getvalue().split('\n')
    decoded_str = contents.decode('utf-8').split('\n') # Decoding contents and
    # using string methods to retrieve the info
    cols = decoded_str[0].split(',') # String methods to obtain name of columns
    # print(cols)
    content = decoded_str[1:-1] # Extracting content for dataframe
    list_df = []
    for element in content: # Loop to create a list with the dataframe content
        list_df.append(
            [float(val) if idx > 0 else val for idx, val in enumerate(element.split(','))]
            )
    df = pd.DataFrame(list_df, columns=cols) # Creating dataframe from list and columns list
    results = {
        'mean1': df['TotSyst_MBD'].mean(),
        'mean2': df['TotSurf_MBD'].mean()
        }
    return results
