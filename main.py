#import libraries
#import numpy as np
import pandas as pd
import pylab as plt

rawData = pd.read_csv("C:/Users/sierr/Documents/GitHub/sunspotdataanalysis/sunspot_data.csv") #73718 rows, 9 columns
#column names: unnamed, year, month, day, date in fraction of year, number of sunspots,
#               standard deviation, observations, indicator

#answer question: what is the cycle of sunspots?

#get lists of the years, and the number of sunspots
years = rawData["Date In Fraction Of Year"]
numberOfSunspots = rawData["Number of Sunspots"]

#locate the maxima, calculate the time between each of the maxima, average them and get uncertainty
#local maxima will be where a value is greater than the values surrounding it
#will need to figure out how to include only the maxima that i mean and not the noise - might have the value be greater than the 10 data points surrounding it

"""diff = np.diff(numberOfSunspots) #doesn't exclude the noise
localMaximaIndices = np.where((diff[:-1] > 0) & (diff[1:] <= 0)) [0] + 1
print(localMaximaIndices.size) 

localMaxIndices = [] #slow, doesn't include endpoints
sep = 75
for i in range(sep,numberOfSunspots.size-sep): #cannot include all of it
    num = numberOfSunspots[i]
    otherNum = [numberOfSunspots[i+x] for x in range(-sep,sep+1) if x!=0]
    if(all(num > otherNum)):
        localMaxIndices.append(i)
print(len(localMaxIndices)) 
#make a list of years and number of sunspots that's just the maxima
maxYears = [years[i] for i in localMaxIndices]
maxNumSunspots = [numberOfSunspots[i] for i in localMaxIndices]
plt.plot(years,numberOfSunspots,'b')
plt.plot(maxYears,maxNumSunspots,'r')
plt.show()
"""

#split up data, find max of those sections
sectionYearBoundaries = [1818.001,1823,1833,1843,1855,1867,1878.5,1889,1901,1912,1923,1933,1944,1954,1964.5,1975.5,1986,1997,2009,2019.832]
sectionBoundariesIndices=[]
j=0
for i in range(len(years)):#get a list of the indices corresponding to the boundaries
    if(abs(years[i] - sectionYearBoundaries[j]) <= 0.001):
        sectionBoundariesIndices.append(i)
        j+=1
#get a list of the max values in each of those sections
maxYears=[]
maxSunspots=[]
for k in range(1,len(sectionBoundariesIndices)):
    #find the max num sunspots in the initialize the correct section
    l = sectionBoundariesIndices[k-1]
    m = sectionBoundariesIndices[k]
    sunspotRange = numberOfSunspots[l:m]
    
    #find the index of the max sunspot
    indexOfMaxNum = sunspotRange.idxmax()
    #find the values corresponding to that index
    maxYears.append(years[indexOfMaxNum])
    maxSunspots.append(numberOfSunspots[indexOfMaxNum])

plt.plot(years,numberOfSunspots,'b',alpha=.5)
plt.plot(maxYears,maxSunspots,'r')
plt.show()

#answer question: what's the cycle of the the maxima itself?
# do fast fourier transform