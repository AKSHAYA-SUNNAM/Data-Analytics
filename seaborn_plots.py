#SEABORN
#-- build on matplotlib to create attractive and more informative statistical graphics

#MATPLOTLIB
## matplotlib is a low-level library for making plots, seaborn is a high-level interface based on matplotlib
## do everything and control everything 
## works with arrays/list, manual support to work with datafreame
# all basic plots
#not interactive

##SEABORN
#-- high level(quick and pretty)
# pandas fataframes
# basic plots + statistical plots(barplot, countplot, pairplot,kde,violin,heatmap,etc)
#not interactive
# provides built in datasets
# customize via matplotlib + **hue,palettes and themes**

import seaborn as sns
import matplotlib.pyplot as plt

##load buildin dataset
# planets = sns.load_dataset("planets")
# planets.info()

flights = sns.load_dataset("flights")
# flights.info()
# print(flights)

titanic = sns.load_dataset("titanic")
# print(titanic.head())

#--> line plot is for: numeric, time series data
sns.lineplot(data=flights,x="year",y="passengers")
plt.title("Yearly passenger details")
plt.show()

#-->bar plot is for: categorical/ non numerical data
    # coparision of classes, groups, categories, regions, products, student etc
    # sns.barplot(data,x,y)
    # not only just plot the bars but also calculate statistics(mean by default) but you can change it to median, sum, etc
sns.barplot(data=flights,x="month",y="passengers")
plt.title("Monthly passenger details")
plt.show()
# hue:
   # split the data into subgroups based on caegorical variable
   #each unique value we will get its own color
sns.barplot(data=flights,x="month",y="passengers", estimator="median",ci=None, hue="month")
plt.show()

#each month is divides into year 
sns.barplot(data=flights,x="month",y="passengers", estimator="median",ci=None, hue="year")
plt.show()

# palette = pastel, deep, rainbow

ax = sns.barplot(data=titanic,x="class",y="fare",hue="age",estimator="median" ,ci= None, palette="pink")
plt.title("Passenger age by class")
plt.show()

   
titanic = sns.load_dataset("titanic")
# show total fare collected for each class separated by gender. display fare values on top of the bars
fig,ax=plt.subplots()
sns.barplot(data=titanic,x="class",y="fare",hue="sex",estimator="median", palette="pink",ax=ax,errorbar=None)
for container in ax.containers:
    ax.bar_label(container,fmt='%.1f')
plt.show()


# pie chart--> percentage or proportion of class/category

## count plot:
     # count/frequency  of the categories
     #sns.countplot(data,x,y)
     # only one categorical variable
sns.countplot(data=titanic, x="class")
plt.title("Count of passengers by class")
plt.show()
# histogram:
      #count/freq of data
      #how?
         # divide the data into bins
         # count how many data points fall into each bin
sns.histplot(data=titanic, x="age", bins=20, kde=True)
plt.title("Age distribution of Titanic passengers")
plt.show()

## SCATTER PLOT

#--> scatter plot is for: 2 numeric variables
# bivariate data
sns.scatterplot(data=titanic,x="fare",y="age",hue="sex",palette="pink")
plt.show()



