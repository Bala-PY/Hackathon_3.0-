# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:18:36 2024

@author: Bala Eesan
"""

# Q1. Factors Influencing Happiness Scores
    
import pandas as pd

df_combined = pd.concat(map(pd.read_csv, ['2015_clean.csv', '2016_clean.csv', '2017_clean.csv',
                                          '2018_clean.csv', '2019_clean.csv']
                            ), 
                        ignore_index = True)
df = df_combined.drop('Region', axis = 1)
df = df.groupby(['Country']).max().round(2)

df = df.nlargest(5, 'Happiness Score') 

df.reset_index().to_csv('plot1_merged.csv', index=False)

df = pd.read_csv('plot1_merged.csv')

y_variable = ["GDP per Capita", "Social Support", "Life Expectancy", "Freedom", "Generosity"
              , "Corruption"]

fig_name = ['H3.1.1.png', 'H3.1.2.png', 'H3.1.3.png', 'H3.1.4.png', 'H3.1.5.png', 'H3.1.6.png']

for index, variables in enumerate(y_variable):
    ax = df.plot.bar(x = 'Country', y = [variables, "Happiness Score"], stacked = True, 
                      title  = 'Happines Score: Top 5 Countries') 
    ax.bar_label(ax.containers[1])
    ax.legend(bbox_to_anchor = (1.0, 1.0))    
    ax.figure.savefig(fig_name[index], bbox_inches = "tight")  
    
# =============================================================================
# Inference: Happiness socre is much proportional to GDP, social support, life 
# expectancy, freedom when compared to generosity and corruption. 
# =============================================================================
