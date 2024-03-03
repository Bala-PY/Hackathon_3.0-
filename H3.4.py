# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:48:18 2024

@author: Bala Eesan
"""

# Q4. Correlation Analysis

import pandas as pd 
import seaborn as sns 

df_combined = pd.concat(map(pd.read_csv, ['2015_clean.csv', '2016_clean.csv', '2017_clean.csv',
                                          '2018_clean.csv', '2019_clean.csv']
                            ), 
                        ignore_index = True)

rem_col = ['Country', 'Region', 'Happiness Rank'] 

df_combined = df_combined.drop(rem_col, axis = 1)

matrix = df_combined.corr()

#plotting correlation matrix 
sns.heatmap(matrix, cmap="Blues", annot = True)

# =============================================================================
# Inference: The correlation plot shows GDP, social support, life expectancy
# and freedom are most significant in determining overall happiness score. 
# =============================================================================
