# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:19:37 2024

@author: Bala Eesan
"""

# Q3. Trends Over Time

import pandas as pd

years = ["2017_clean.csv", "2018_clean.csv", "2019_clean.csv"]

year_now = 2017

fig_name = ['H3.3.1.png', 'H3.3.2.png', 'H3.3.3.png', 'H3.3.4.png', 'H3.3.5.png']

for index, year in enumerate(years): 
    df = pd.read_csv(year)
    region_of_interest = ['South America', 'Australia']
    filter_df = df[df['Region'].isin(region_of_interest)]
    filter_df = filter_df.nlargest(3, 'Happiness Score') 
    filter_df.to_csv('plot3.csv', index=False)
    df = pd.read_csv('plot3.csv')
    df = df.round(2)
    ax = df.plot.bar(x = 'Country', y = ["Life Expectancy","Happiness Score"], stacked = True,
                     title = "Year {year}".format(year = year_now))
    ax.bar_label(ax.containers[0])
    ax.legend(bbox_to_anchor=(1.0, 1.0))
    
    ax.figure.savefig(fig_name[index], bbox_inches = "tight")
    
    year_now += 1

# =============================================================================
# Inference: A continuous increase in life expectancy over the years 2017-2019 
# might have caused a trend change in happiness disparities for SA and AU.
# =============================================================================
