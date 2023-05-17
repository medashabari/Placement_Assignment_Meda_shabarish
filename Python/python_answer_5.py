import requests 
import os
import pandas as pd 
from datetime import datetime
def download_data(url):
    # sending a get request to the url and retrieving
    response = requests.get(url)
    data = response.json()
    return data 

def extract_json_data(data):
    # accessing the episodes data inside the main show data
    episodes = data["_embedded"]["episodes"]
    extracted_data = []
    for episode in episodes:
        episode_data = {}
        episode_data["id"] = episode["id"]
        episode_data["url"] = episode["url"]
        episode_data["name"] = episode["name"]
        episode_data["season"] = episode["season"]
        episode_data["number"] = episode["number"]
        episode_data["type"] = episode["type"]

        # Format the airdate to date format
        airdate_str = episode["airdate"]
        episode_data["airdate"] = datetime.strptime(airdate_str, "%Y-%m-%d").date()

        # Format the airtime to 12-hour time format
        airtime_str = episode["airtime"]
        episode_data["airtime"] = datetime.strptime(airtime_str, "%H:%M").strftime("%I:%M %p")

        episode_data["runtime"] = episode["runtime"]
        episode_data["average_rating"] = episode["rating"]["average"]
        episode_data["summary"] = episode["summary"].strip("<p>").strip("</p>")
        episode_data["medium_image_link"] = episode["image"]["medium"]
        episode_data["original_image_link"] = episode["image"]["original"]
        episode_data['self_href'] = episode["_links"]['self']['href']
        episode_data['show_href'] = episode["_links"]['show']['href']
        extracted_data.append(episode_data)
    return extracted_data
def save_as_excel(df,output_file):
     # creating the dataset folder if not exists
    os.makedirs("dataset/",exist_ok=True)
    # conveting to excel file and saving it in dataset folder
    df.to_excel("dataset/"+output_file,index=False)

url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

data = download_data(url) # download data

extracted_data = extract_json_data(data) # convert to df

extracted_data = pd.DataFrame(extracted_data)

output_file = "movie_shows.xlsx"

save_as_excel(extracted_data, output_file) # save as excel file

print("Successfully dowloaded movie shows json data")