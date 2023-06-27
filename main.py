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

#locate the maxima, calculate the time between each of the maxima, average them and get uncertainty
#local maxima will be where a value is greater than the values surrounding it
#will need to figure out how to include only the maxima that i mean and not the noise - might have the value be greater than the 10 data points surrounding it
diff = np.diff(numberOfSunspots) #this doesn't fix it
localMaximaIndices = np.where((diff[:-1] > 0) & (diff[1:] <= 0)) [0] + 1

#answer question: what's the cycle of the the maxima itself?
# do fast fourier transform