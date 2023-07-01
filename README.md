# Overview

I wanted more practice in data analysis, so I decided to work on this project. This data contains the number of sunspots that are observed each day. Sunspots are areas on the sun that appear darker. This is because they are significantly colder than the surrounding areas. Strong magnetic fields in the sun prevent convection in that area, meaning that those particular particles are not heated as much as the rest of the sun. There is a cycle in sunspots because the sun's magnetic flip, and the north and south switch places. During that process, the changing magnetic fields cause the sunspot activity to change. 

I obtained my data [here](https://www.kaggle.com/datasets/abhinand05/daily-sun-spot-data-1818-to-2019?resource=download) on Kaggle. The data includes the number of sunspots and the time in years, among other values. 


Below is a link to a demonstration of my code.

[Software Demo Video](https://www.youtube.com/watch?v=zT3IXTWs_1E)

# Data Analysis Results

In this data analysis, I sought to answer a few questions.
My first question was: What is the cycle of sunspots, as described by this data? I calculated that the mean cycle length, as described by the data, is 10.87 years. 

My second question was: What is the predicted activity in this month, June 2023, according to the trends from this data?
I calcualted that the number of sunspots that are predicted for June 30, 2023 are 127 sunspots, give or take 21 sunspots. I made a few important assumptions as I performed these calculations. One assumption is that the end of the data is a minimum in the cycle of sunspots. Another assumption is that the time between a minimum and a maximum in the cycle is exactly half of the length of a cycle. I feel confident making these assumptions. 

# Development Environment

I used Visual Studio Code as well as Spyder to write this code. The language that I used was Python, and I accessed the numpy, pandas, and pylab libraries. 

# Useful Websites

The following are a few helpful websites. 

* [Kaggle](https://www.kaggle.com/datasets/abhinand05/daily-sun-spot-data-1818-to-2019?resource=download)
* [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html)
* [ChatGPT](https://chat.openai.com/)

# Future Work

* Determine a trend that describes the value of the maxima as a function of time. 
* Perform claculations again with updated data.