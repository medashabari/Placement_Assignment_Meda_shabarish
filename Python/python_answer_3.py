import requests 
import os
import pandas as pd 

def download_data(url):
    # sending a get request to the url and retrieving
    response = requests.get(url)
    data = response.json()
    return data 

def convert_to_df(data):
    # accessing the pokemen data inside the pokemen key
    relvant_data = data['pokemon']
    return pd.json_normalize(relvant_data)

def save_as_excel(df,output_file):
     # creating the dataset folder if not exists
    os.makedirs("dataset/",exist_ok=True)
    # conveting to excel file and saving it in dataset folder
    df.to_excel("dataset"+output_file,index=False)

url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

data = download_data(url) # download data

df = convert_to_df(data) # convert to df

output_file = "pokeman_data.xlsx"

save_as_excel(df, output_file) # save as excel file

print("Successfully dowloaded pokeman json data")