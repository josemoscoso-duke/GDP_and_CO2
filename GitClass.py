import pandas as pd
wdi_2015 = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')

wdi_2015 = wdi_2015[["Mortality rate, infant (per 1,000 live births)","GDP per capita (constant 2010 US$)","Country Name"]]





