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

#py.plot(years,numberOfSunspots)
#py.show()

#locate the maxima, calculate the time between each of the maxima, average them and get uncertainty
#local maxima will be where a value is greater than the values surrounding it
#will need to figure out how to include only the maxima that i mean and not the noise - might have the value be greater than the 10 data points surrounding it

diff = np.diff(numberOfSunspots) #doesn't exclude the noise
localMaximaIndices = np.where((diff[:-1] > 0) & (diff[1:] <= 0)) [0] + 1
print(localMaximaIndices.size)

localMaxIndices = [] #slow, doesn't include endpoints
for i in range(1,numberOfSunspots.size-1): #cannot include all of it
    num = numberOfSunspots[i]
    otherNum = [numberOfSunspots[x] for x in [i-1,i+1]]
    if(all(num > otherNum)):
        localMaxIndices.append(i)
print(len(localMaxIndices))


#answer question: what's the cycle of the the maxima itself?
# do fast fourier transform