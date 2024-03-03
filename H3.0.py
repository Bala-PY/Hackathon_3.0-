# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:11:53 2024

@author: Bala Eesan
"""

import pandas as pd

#data_cleaning - Year 2015 ---- START

df_2015 = pd.read_csv('2015.csv')

region_key = set(df_2015['Region'].to_list())
region_value = ['Europe', 'Australia', 'North America', 'Europe', 'Asia',
                'Asia', 'Asia', 'Africa', 'South America', 'Africa']

region_dict = dict(zip(region_key,region_value))

for index, regions in enumerate(df_2015['Region']):
    df_2015['Region'].values[index] = region_dict[regions]

df_2015.rename(columns = {'Economy (GDP per Capita)':'GDP per Capita','Family':'Social Support', 'Health (Life Expectancy)':'Life Expectancy','Trust (Government Corruption)':'Corruption'}, inplace = True)
df_2015 = df_2015.drop(['Standard Error'], axis=1)
df_2015.insert(8, 'Generosity', df_2015.pop('Generosity'))
  
df_2015.to_csv('2015_clean.csv', index = False)

    #data_cleaning - Year 2015 ---- END

#data_cleaning - Year 2016 ---- START

df_2016 = pd.read_csv('2016.csv')

region_key = set(df_2016['Region'].to_list())
region_value = ['Europe', 'Australia', 'North America', 'Europe', 'Asia',
                'Asia', 'Asia', 'Africa', 'South America', 'Africa']

region_dict = dict(zip(region_key,region_value))

for index, regions in enumerate(df_2016['Region']):
    df_2016['Region'].values[index] = region_dict[regions]

df_2016.rename(columns = {'Economy (GDP per Capita)':'GDP per Capita','Family':'Social Support','Health (Life Expectancy)':'Life Expectancy','Trust (Government Corruption)':'Corruption'}, inplace = True)
df_2016 = df_2016.drop(['Lower Confidence Interval', 'Upper Confidence Interval'], axis=1)
df_2016.insert(8, 'Generosity', df_2016.pop('Generosity'))
  
df_2016.to_csv('2016_clean.csv', index = False)

    #data_cleaning - Year 2016 ---- END
    
#data_cleaning - Year 2017 ---- START

df_2017 = pd.read_csv('2017.csv')
df_2015 = pd.read_csv('2015.csv')

country_list = df_2015['Country'].to_list()
region_list = df_2015['Region'].to_list()

region = []

region_dict = dict(zip(country_list,region_list))

for index, entry in enumerate(df_2017['Country']):
    try:
        region.append(region_dict[entry])
    except KeyError:
        df_2017 = df_2017.drop(index, axis = 0)

df_2017.insert(1, 'Region', region)

region_key = set(df_2017['Region'].to_list())
region_value = ['Europe', 'Australia', 'North America', 'Europe', 'Asia',
                'Asia', 'Asia', 'Africa', 'South America', 'Africa']

region_dict = dict(zip(region_key,region_value))

for index, regions in enumerate(df_2017['Region']):
    df_2017['Region'].values[index] = region_dict[regions]

df_2017.rename(columns = {'Happiness.Rank': 'Happiness Rank','Happiness.Score':'Happiness Score','Economy..GDP.per.Capita.':'GDP per Capita','Family':'Social Support','Health..Life.Expectancy.':'Life Expectancy','Trust..Government.Corruption.':'Corruption','Dystopia.Residual':'Dystopia Residual'}, inplace = True)
df_2017 = df_2017.drop(['Whisker.high', 'Whisker.low'], axis=1)

df_2017.to_csv('2017_clean.csv', index = False)

    #data_cleaning - Year 2017 ---- END

#data_cleaning - Year 2018 ---- START

df_2018 = pd.read_csv('2018.csv')
df_2015 = pd.read_csv('2015.csv')

country_list = df_2015['Country'].to_list()
region_list = df_2015['Region'].to_list()

region = []

region_dict = dict(zip(country_list,region_list))

for index, entry in enumerate(df_2018['Country or region']):
    try:
        region.append(region_dict[entry])
    except KeyError:
        df_2018 = df_2018.drop(index, axis = 0)

df_2018.insert(1, 'Region', region)

region_key = set(df_2018['Region'].to_list())
region_value = ['Europe', 'Australia', 'North America', 'Europe', 'Asia',
                'Asia', 'Asia', 'Africa', 'South America', 'Africa']

region_dict = dict(zip(region_key,region_value))

for index, regions in enumerate(df_2018['Region']):
    df_2018['Region'].values[index] = region_dict[regions]

df_2018.rename(columns = {'Overall rank': 'Happiness Rank', 'Country or region': 'Country', 'Score':'Happiness Score', 'GDP per capita':'GDP per Capita', 'Social support':'Social Support', 'Healthy life expectancy':'Life Expectancy','Freedom to make life choices':'Freedom', 'Perceptions of corruption':'Corruption'}, inplace = True)
df_2018.insert(0, 'Country', df_2018.pop('Country'))
df_2018.insert(2, 'Happiness Rank', df_2018.pop('Happiness Rank'))

df_2018.to_csv('2018_clean.csv', index = False)

    #data_cleaning - Year 2018 ---- END
    
#data_cleaning - Year 2019 ---- START

df_2019 = pd.read_csv('2019.csv')
df_2015 = pd.read_csv('2015.csv')

country_list = df_2015['Country'].to_list()
region_list = df_2015['Region'].to_list()

region = []

region_dict = dict(zip(country_list,region_list))

for index, entry in enumerate(df_2019['Country or region']):
    try:
        region.append(region_dict[entry])
    except KeyError:
        df_2019 = df_2019.drop(index, axis = 0)

df_2019.insert(1, 'Region', region)

region_key = set(df_2019['Region'].to_list())
region_value = ['Europe', 'Australia', 'North America', 'Europe', 'Asia',
                'Asia', 'Asia', 'Africa', 'South America', 'Africa']

region_dict = dict(zip(region_key,region_value))

for index, regions in enumerate(df_2019['Region']):
    df_2019['Region'].values[index] = region_dict[regions]

df_2019.rename(columns = {'Overall rank': 'Happiness Rank', 'Country or region': 'Country', 'Score':'Happiness Score', 'GDP per capita':'GDP per Capita', 'Social support':'Social Support', 'Healthy life expectancy':'Life Expectancy','Freedom to make life choices':'Freedom', 'Perceptions of corruption':'Corruption'}, inplace = True)
df_2019.insert(0, 'Country', df_2019.pop('Country'))
df_2019.insert(2, 'Happiness Rank', df_2019.pop('Happiness Rank'))

df_2019.to_csv('2019_clean.csv', index = False)

    #data_cleaning - Year 2019 ---- END