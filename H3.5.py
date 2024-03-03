# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:26:25 2024

@author: Bala Eesan
"""

# Q5. Government Policies and Happiness
    
import pandas as pd
import seaborn as sns 

df_combined = pd.concat(map(pd.read_csv, ['2015_clean.csv', '2016_clean.csv', '2017_clean.csv',
                                          '2018_clean.csv', '2019_clean.csv']
                            ), 
                        ignore_index = True)
df_combined.rename(columns = {'Corruption':'Government Policy Score'}, inplace = True)

region_of_interest = ['South America', 'Australia']
filter_df = df_combined[df_combined['Region'].isin(region_of_interest)]
filter_df = filter_df.nlargest(15, 'Happiness Score') 
filter_df.to_csv('plot5.csv', index=False)

rem_col = ['Country', 'Region', 'Happiness Rank', 'GDP per Capita', 'Social Support',
           'Life Expectancy', 'Freedom', 'Generosity', 'Dystopia Residual'] 

df = df_combined.drop(rem_col, axis = 1)

matrix = df.corr()

#plotting correlation matrix 
sns.heatmap(matrix, cmap="Blues", annot = True)

# =============================================================================
# Inference: Government policy influence on the overall happiness score is less 
# than 0.5 in our region of interest South America and Australia.
# =============================================================================
