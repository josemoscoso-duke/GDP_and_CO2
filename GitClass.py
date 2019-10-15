#import urllib.request

#print('Beginning file download with urllib2...')

#url = 'https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv'
#data1 = urllib.request.urlretrieve(url, 'E:/Jose_Moscoso/Duke/GitHub/GDP_and_CO2/wdi_2015')
#response = urllib2.urlopen('http://www.example.com/')
#data = urllib2.urlopen("https://github.com/nickeubank/MIDS_Data/raw/master/World_Development_Indicators/raw_WDI_Data_csv.zip")


import pandas as pd
wdi_2015 = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')

wdi_2015 = wdi_2015[["Mortality rate, infant (per 1,000 live births)","GDP per capita (constant 2010 US$)","Country Name"]]





