# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:34:49 2024

@author: Bala Eesan
"""

# Q2. Regional Happiness Disparities for Years 2015-2019

import pandas as pd

years = ["2015_clean.csv", "2016_clean.csv", "2017_clean.csv", "2018_clean.csv", "2019_clean.csv"]

year_now = 2015

for year in years:
    df = pd.read_csv(year)
    df = df.drop('Country', axis = 1)
    df = df.groupby('Region').min().round(2)
    df = df.sort_values("Happiness Rank")
    df.reset_index().to_csv("plot2.csv", index = False)

    for index, rank in enumerate(df['Happiness Rank']):
        df['Happiness Rank'].values[index] = index+1

    df = df.reset_index()

    ax = df.plot.bar(x = 'Region', y = "Happiness Rank", title = "Year {year}".
                     format(year = year_now)) 
    ax.bar_label(ax.containers[0])

    ax.invert_yaxis()
    year_now += 1
    
# =============================================================================
# Inference: The regional happiness disparities remains the same for the years 
# 2015-2017. A change in the ranking order is noticed for years 2018 and 2019.
# =============================================================================
