import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import linear_model, ensemble, tree, datasets, cross_validation
from sklearn import grid_search
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project Luther")

# Movie ticket Inflation
url = "http://www.boxofficemojo.com/about/adjuster.htm"

df1 = pd.read_html(url)
inflation = pd.Series({2015: 8.43, 2014: 8.17, 2013: 8.13, 2012: 7.96, 2011: 7.93, \
                       2010: 7.89, 2009: 7.50, 2008: 7.18, 2007: 6.88, 2006: 6.55, \
                       2005: 6.41, 2004: 6.21, 2003: 6.03, 2002: 5.81, 2001: 5.66, 2000: 5.39})
inflation_index = inflation/5.39


# Final DataFrame clean up
data = pd.read_csv("final_data.csv")
data = data.dropna()
del(data["Index"])
del(data["Title"])
data["Release Date"] = pd.to_datetime(data["Release Date"])
data["Year"] = data["Release Date"].dt.year
data["Gross Adjusted"] = data["Gross Sales"]/data["Inflation Index"]
del(data["Release Date"])
data = data[data["Year"] >= 2000]
del(data["Year"])
del(data["Tickets Sold"])
runtime = [int(i.strip(" min")) for i in list(data["Runtime"])]
data["Runtime"] = runtime
mpaa = pd.get_dummies(data["MPAA"])
genre = pd.get_dummies(data["Genre"])
distributor = pd.get_dummies(data["Distributor"])
data = pd.concat([data, mpaa, genre, distributor], axis = 1)
data_body = data.drop("Gross Sales", axis = 1)
data_body = data_body.drop("Gross Adjusted", axis = 1)
data_body = data_body.drop("Distributor", axis = 1)
data_body = data_body.drop("Genre", axis = 1)
data_body = data_body.drop("MPAA", axis = 1)
data_body = data_body.drop("Inflation Index", axis = 1)


# Regression Analysis
models = {}
models['ridge'] = linear_model.Ridge()
models['lasso'] = linear_model.Lasso(alpha = .2)
models['elasticnet'] = linear_model.ElasticNet()

X_train, X_test, y_train, y_test = cross_validation.train_test_split(
                                    data_body, data["Gross Adjusted"], test_size = 0.3)
for name, model in models.items():
    model.fit(X_train,y_train)
    print('Model: ' + name)
    print("Score: " + str(model.score(X_test, y_test)))
    sorted_features = sorted(zip(data_body.columns, model.coef_), key = lambda tup: abs(tup[1]), reverse = True)
    for feature in sorted_features:
        print(feature)
    print("")

data_body.to_csv("plotly.csv")

#if time allows, include kfold or shufflesplit for random testing and output graphs and try different regressions

# Scatter Matrix Visualization
import plotly.plotly as py
from plotly.tools import FigureFactory as FF

fig = FF.create_scatterplotmatrix(data_body, height=800, width=800)
py.iplot(fig, filename='Scatterplot Matrix')
