# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:18:04 2018

@author: Malini
"""
"""Read the dataset from the below link
#https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US
_Baby_Names/US_Baby_Names_right.csv"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read in small data from .csv file
# Filepath
df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
print(df)
print('Shape', df.shape)
print('-------------------------')
print('Number of rows', len(df))
print('-------------------------')
print('Column headers', df.columns)
print('-------------------------')
print('Data types', df.dtypes)
print('-------------------------')
print('Index', df.index)
print('-------------------------')

#1. Delete unnamed columns
df = df.drop('Unnamed: 0', 1)
print(df)
#2 Show the distribution of male and female
df.groupby('Gender').Year.hist()
print(df)
#3 Show the top 5 most preferred names
df1= df['Name'].value_counts()
df1.head(5)
#4 What is the median name occurrence in the dataset
df1= df['Name'].value_counts()
print(df1)
print("Median name occurrence in the dataset:",df1.median())
#5 Distribution of male and female born count by states
impute_grps = df.pivot_table(values=["Count"], index=["Gender","State"], aggfunc=np.mean)
print(impute_grps)

