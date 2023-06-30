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
sectionYearBoundaries = [1818.001,1823,1833,1843,1855,1867,1878.5,1889,1901,\
                         1912,1923,1933,1944,1954,1964.5,1975.5,1986,1997,\
                             2009,2019.832] #values found visually
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

#make a plot to visualize the maxima
plt.figure(1)
plt.plot(years,numberOfSunspots,'b',alpha=.5, label="Raw Data")
plt.plot(maxYears,maxSunspots,'r', label="Peaks")

plt.xlabel('Year') #axis labels
plt.ylabel('Number of sun spots')
plt.legend()
plt.show()

cycleData = np.diff(maxYears)
avgCycle = np.mean(cycleData)
uncertCycle = np.std(cycleData) / np.sqrt(len(cycleData))

print("The average cycle of sunspots are {:.3f} +- {:.3f} years long.".format(avgCycle, uncertCycle))

##############################################################################################
#Question: According to this data, what is the predicted activity in this month, June 2023?
#note that we are assuming that the end of this data is a local minimum, 
#and we are also assuming that a minimum to a peak is exactly half of a cycle.
#date that we are forecasting for: June 30, 2023 = 2023.495 years

#determine years between june 30 and end of data set
June30InYears = 2023.495
endOfData = years.iloc[-1]
diffInYears = June30InYears - endOfData #time between a minimum and June 30th
timeUntilPeak = (avgCycle/2) - diffInYears #time between June 30th and the porjected maximum

#get the number of sunspots at the same time of the cycle as June 30th
#need to round to three decimal places for the comparison with the years
yearsFromPast = np.around(np.array(maxYears[1:]) - timeUntilPeak, 3)

sunspotsFromPast = []
for value in yearsFromPast:
    if value in years.values:
        something = years[years == value]
        #exclude the negative values, valid numbers are always positive
        if (numberOfSunspots[something.index[0]] > -1): sunspotsFromPast.append(numberOfSunspots[something.index[0]]) 
        
    
#get min, max, mean
pastSunspotsSeries = pd.Series(sunspotsFromPast) #turning the list into a series is easier for calculations

june30Min = pastSunspotsSeries.min()
june30Max = pastSunspotsSeries.max()
june30Mean = pastSunspotsSeries.mean()
june30MeanUncert = np.std(pastSunspotsSeries) / np.sqrt(len(pastSunspotsSeries))

print("The mean number of sunspots on a day like June 30, 2023 is {:.0f} +- {:.0f}.".capitalize().format(june30Mean,june30MeanUncert))
print("The range of numbers of sunspots are {} - {}".format(june30Min, june30Max))

#make a box and whisker plot of the number of sunspots
data = {' ':sunspotsFromPast}
df= pd.DataFrame(data)
plt.figure(2)
df.boxplot()
plt.title("Number of Sunspots on days similar to June 30, 2023")
plt.xlabel("Days like June 30,2023")
plt.ylabel("Number of Sunspots")
plt.show()