# filter for USA, English movies, movies,
# Metascore, MPAA Ratings, Runtime, Release Date, IMDB Rating, IMDB Votes, tickets sold, Studio Name
# Incorporate GDP Deflator
# Dependent Variable = gross sales,

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project Luther")

numbersdf = pd.read_csv("the_numbers.csv")

omdb1df = pd.read_csv("omdb.csv")
omdb2df = pd.read_csv("omdb1.csv")
omdbdf = pd.concat([omdb1df, omdb2df], axis = 0)

del omdbdf["Actors"]
del omdbdf["Awards"]
del omdbdf["Error"]
del omdbdf["Number"]
del omdbdf["Plot"]
del omdbdf["Poster"]
del omdbdf["Response"]
del omdbdf["Unnamed: 0"]
del omdbdf["Unnamed: 23"]
del omdbdf["Writer"]
del omdbdf["Genre"]
del omdbdf["Director"]
del omdbdf["imdbID"]
del omdbdf["totalSeasons"]
omdbdf = omdbdf[omdbdf["Type"] == "movie"]
omdbdf = omdbdf[omdbdf["Year"] >= "2000"]
omdbdf = omdbdf[omdbdf["Runtime"] >= "30"]
omdbdf = omdbdf[omdbdf["Language"] == "English"]
omdbdf = omdbdf[omdbdf["Country"] == "USA"]
del omdbdf["Year"]
del omdbdf["Type"]
del omdbdf["Country"]
del omdbdf["Language"]
del omdbdf["Released"]
del omdbdf["Rated"]
omdbdf = omdbdf.dropna()
omdbdf.to_csv("omdb_final.csv")
