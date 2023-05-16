import pandas as pd
import requests
import os


def download_data(url):
    # sending a get request to the url
    response = requests.get(url)
    data = response.json()
    return data


def convert_to_df(data):
    # coverting to dataframe
    df = pd.DataFrame(data)
    df.drop([':@computed_region_cbhk_fwbd',':@computed_region_nnqa_25f4'],axis=1,inplace=True)
    return df
    


def save_as_csv(df, output_file):
    # creating the dataset folder if not exists
    os.makedirs("dataset", exist_ok=True)
    # conveting to csv file and saving it in dataset folder
    df.to_csv("dataset/"+output_file, index=False)


url = "https://data.nasa.gov/resource/y77d-th95.json"  # URL

data = download_data(url)  # download data
columns = ['name',]
df = convert_to_df(data)  # conveting to dataframe

output_file = "nasa_data.csv"

save_as_csv(df, output_file)  # saving as csv

print("Successfully dowloaded and saved the nasa data")
