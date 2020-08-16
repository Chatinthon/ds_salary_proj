# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:55:37 2020

@author: Chatinthon
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/hp/Desktop/scrapping/chromedriver"


df = gs.get_jobs('Data Science',1000,False,path,15)

df.to_csv(r'C:\Users\hp\Desktop\scrapping\datascience_glassdoor.csv', index = False)