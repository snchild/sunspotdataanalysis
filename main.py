#import libraries
import numpy as np
import pandas as pd
import pylab as plt

rawData = pd.read_csv("C:/Users/sierr/Documents/GitHub/sunspotdataanalysis/sunspot_data.csv") #73718 rows, 9 columns
#column names: unnamed, year, month, day, date in fraction of year, number of sunspots,
#               standard deviation, observations, indicator
##############################################################################################
#Question: what is the cycle of sunspots?

#get lists of the years, and the number of sunspots
years = rawData["Date In Fraction Of Year"]
numberOfSunspots = rawData["Number of Sunspots"]


#locate the maxima, calculate the time between each of the maxima, average them and get uncertainty

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

plt.figure(1)
plt.plot(years,numberOfSunspots,'b',alpha=.5, label="Raw Data")
plt.plot(maxYears,maxSunspots,'r', label="Peaks")

plt.xlabel('Year') #axis labels
plt.ylabel('Number of sun spots')
plt.legend()
plt.show()

avgCycle = np.mean(np.diff(maxYears))

print("The average cycle of sunspots are ", avgCycle ," years long")

##############################################################################################
#Question: According to this data, what is the predicted activity in this month, June 2023?
#note that we are assuming that the end of this data is a local minimum, and we are also assuming that a minimum to a peak is exactly half of a cycle.
#date that we are forecasting for: June 30, 2023
#in years, this is 2023.495

#determine years between june 30 and end of data set
June30InYears = 2023.495
endOfData = years.iloc[-1]
diffInYears = round(June30InYears - endOfData, 3) #makes sure the difference is rounded to three decimal places
#determine how far that is from the peak of the cycle
timeUntilPeak = round((avgCycle/2) - diffInYears, 3)


#get the values of the trend at that time
valuesFromPast = np.array(maxYears[1:]) - timeUntilPeak
#def isLateEnough(n):
#    return n > years[0]
#filteredValuesFromPast = list(filter(isLateEnough, valuesFromPast))

indicesFromPast = []
for value in valuesFromPast:
    indicesFromPast.append(years.index[years == value].tolist()[0])
print(indicesFromPast)
#get min, max, mean
#calculate uncertainty