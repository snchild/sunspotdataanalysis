#import libraries
import numpy as np
import pandas as pd
import pylab as py

rawData = pd.read_csv("sunspot_data.csv") #73718 rows, 9 columns
#column names: unnamed, year, month, day, date in fraction of year, number of sunspots,
#               standard deviation, observations, indicator

#answer question: what is the cycle of sunspots?

#get lists of the years, and the number of sunspots
years = rawData["Date In Fraction Of Year"]
numberOfSunspots = rawData["Number of Sunspots"]

py.plot(years,numberOfSunspots)
py.show()