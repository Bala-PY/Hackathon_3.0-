# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:34:49 2024

@author: Bala Eesan
"""

# Q2. Regional Happiness Disparities for Years 2015-2019

import pandas as pd

years = ["2015_clean.csv", "2016_clean.csv", "2017_clean.csv", "2018_clean.csv", "2019_clean.csv"]

year_now = 2015

fig_name = ['H3.2.1.png', 'H3.2.2.png', 'H3.2.3.png', 'H3.2.4.png', 'H3.2.5.png']

for index1, year in enumerate(years):
    df = pd.read_csv(year)
    df = df.drop('Country', axis = 1)
    df = df.groupby('Region').min().round(2)
    df = df.sort_values("Happiness Rank")
    df.reset_index().to_csv("plot2.csv", index = False)

    for index2, rank in enumerate(df['Happiness Rank']):
        df['Happiness Rank'].values[index2] = index2+1

    df = df.reset_index()

    ax = df.plot.bar(x = 'Region', y = "Happiness Rank", title = "Year {year}".
                     format(year = year_now)) 
    ax.bar_label(ax.containers[0])

    ax.invert_yaxis()
    ax.figure.savefig(fig_name[index1], bbox_inches = "tight")
    
    year_now += 1
    
# =============================================================================
# Inference: The regional happiness disparities remains the same for the years 
# 2015-2017. A change in the ranking order is noticed for years 2018 and 2019.
# =============================================================================
