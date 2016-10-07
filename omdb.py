import pandas as pd
import requests
import json
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project Luther")

titles = []
with open("movie_titles.csv") as f:
    for i in f:
        titles.append(i)
        titles = [j.replace(" ", "+") for j in f]
# print(titles)

#already scraped
"""
omdb = pd.DataFrame()
for row in range(len(titles)):
    title = titles[row].lower()
    url = "http://www.omdbapi.com/?t=" + str(title)
    response = requests.get(url)
    var = json.loads(response.text)
    json_dict = pd.DataFrame(list(var.items()))
    json_dict = json_dict.set_index(json_dict[0])
    json_dict = json_dict.transpose()
    json_dict = json_dict[1:]
    omdb = pd.concat([omdb,json_dict])

omdb.to_csv("omdb.csv")
"""

titles1 = []
with open("movie_titles1.csv") as f1:
    for i in f1:
        titles1.append(i)
        titles1 = [j.replace(" ", "+") for j in f1]
# print(titles1)

omdb1 = pd.DataFrame()
for row1 in range(len(titles1)):
    title1 = titles1[row1].lower()
    url1 = "http://www.omdbapi.com/?t=" + str(title1)
    response1 = requests.get(url1)
    var1 = json.loads(response1.text)
    json_dict1 = pd.DataFrame(list(var1.items()))
    json_dict1 = json_dict1.set_index(json_dict1[0])
    json_dict1 = json_dict1.transpose()
    json_dict1 = json_dict1[1:]
    omdb1 = pd.concat([omdb1,json_dict1])

omdb1.to_csv("omdb1.csv")
