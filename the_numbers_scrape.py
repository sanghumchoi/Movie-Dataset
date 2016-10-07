import requests
import pandas as pd
from bs4 import BeautifulSoup

def souping(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    title = []
    release_date = []
    distributor = []
    genre = []
    mpaa = []
    tickets_sold = []
    gross_sales = []

    for row in soup.find_all("tr")[1:-2]:
        col = row.find_all("td")
        column1 = col[1].string.strip()
        title.append(column1)
        column2 = col[2].string.strip()
        release_date.append(column2)
        column3 = col[3].string
        distributor.append(column3)
        column4 = col[4].string
        genre.append(column4)
        column5 = col[5].string.strip()
        mpaa.append(column5)
        column6 = col[7].string.strip()
        tickets_sold.append(column6)
        column7 = col[6].string.strip()
        gross_sales.append(column7)

    columns = {"Title": title, "Release Date": release_date, "Distributor": distributor, "Genre": genre, "MPAA": mpaa, "Tickets Sold": tickets_sold, "Gross Sales": gross_sales}
    df = pd.DataFrame(columns)
    return df

the_numbers_movies = pd.DataFrame()

for i in range(2000,2016):
    url = "http://www.the-numbers.com/market/" + str(i) + "/top-grossing-movies"
    top = souping(url)
    the_numbers_movies = pd.concat([the_numbers_movies,top], axis = 0)

the_numbers_movies.to_csv("the_numbers.csv")
