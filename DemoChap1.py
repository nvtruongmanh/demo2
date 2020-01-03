# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:11:28 2019

@author: Admin
"""
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Ch 1. Data and Statistics
# Import Minisystems data into pandas
minisystems = pd.read_excel( io=r'C:\Users\Admin\OneDrive\Education\Probability Statistics\20191223_Statistcs for Business and Economics - Anderson - Sweeney - Williams\Resources\Ch 01 Data and Statistics\Minisystems.xlsx', 
                         sheet_name='Data')
# so phan tu trong Minisystems
len(minisystems)

# Price mean
minisystems.columns
minisystems.describe()
minisystems['Price ($)'].mean()

# the number of columns
minisystems.shape

# the average CD Capacity
minisystems['CD Capacity'].mean()


# Value-counts: to understanding how many units of each variable
minisystems['FM Tuning'].value_counts()
minisystems['FM Tuning'].value_counts().to_frame()
fmtuning = minisystems['FM Tuning'].value_counts().to_frame()
fmtuning.rename(columns={'FM Tuning': 'value counts'}, inplace=True)

# The Percentage of FM Tunin
fmtuning['Percentage'] = fmtuning['value counts']/fmtuning['value counts'].sum()

# The Percentage of CD Capacity
cdcapacity = minisystems['CD Capacity'].value_counts().to_frame()
cdcapacity.rename(columns={'CD Capacity': 'value counts'}, inplace=1)
cdcapacity['Percentage'] = cdcapacity['value counts']/cdcapacity['value counts'].sum()


####### 25. Bo du lieu thong tin ve 25 loai co phieu

shadow02 = pd.read_excel( io=r'C:\Users\Admin\OneDrive\Education\Probability Statistics\20191223_Statistcs for Business and Economics - Anderson - Sweeney - Williams\Resources\Ch 01 Data and Statistics\Shadow02.xlsx', 
                         sheet_name='Data')

# Build a bin array

bins = np.linspace(0,74.9,6)
group_names = ['0-14.9', '15-29.9', '30-44.9', '45-59.9', '60-74.9']
shadow02['Gross Profit Margin (%)-binned'] = pd.cut(shadow02['Gross Profit Margin (%)'],
        bins, labels=group_names, include_lowest=True)

shadow02['Gross Profit Margin (%)-binned'] = sorted(shadow02['Gross Profit Margin (%)-binned'])

GPM_binned = shadow02['Gross Profit Margin (%)-binned'].value_counts().sort_index().to_frame()

plt.hist(shadow02['Gross Profit Margin (%)-binned'])

# Average Price/Earnings Ratio
shadow02['Price/Earnings Ratio'].mean()



shadow02.columns.to_list()
