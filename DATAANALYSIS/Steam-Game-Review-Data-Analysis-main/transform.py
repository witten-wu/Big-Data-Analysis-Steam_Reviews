#!/usr/bin/env python

# this module contains functions for transforming data
import pandas as pd
import json
import sys
from datetime import datetime

#print(pd.__version__)

# takes unix timestamp and converts to string "yyyy-mm-dd"
def timestamp_to_date(timestamp):
    timestamp = timestamp.astype(int)
    timestamp = [datetime.fromtimestamp(x) for x in timestamp]
    strdate = [i.strftime("%Y-%d-%m") for i in timestamp]
    return strdate

# takes release release_date of game (i.e "18 Apr, 2011") and total number of reviews of game and predicts number of sales based off of "NB number"
# median NB number 58 sales per review
# <2017 74 sales per review
# 2017 63 sales per review
# 2018
# 2019 51 sales per review
# 2020 (early) 38 sales per review
# 2020 (late) 20 sales per review
def reviews_to_sales(release_date, num_reviews):
    try:
        #print(release_date, num_reviews)
        #release_date = datetime.strptime(release_date, '%d %b, %Y')
        if release_date < datetime(2017,1,1):
            return num_reviews * 74
        elif release_date > datetime(2016,12,31) and release_date < datetime(2018,1,1):
            return num_reviews * 63
        elif release_date > datetime(2017,12,31) and release_date < datetime(2019,1,1):
            return num_reviews * 52
        elif release_date > datetime(2018,12,31) and release_date < datetime(2020,1,1):
            return num_reviews * 51
        elif release_date > datetime(2019,12,31) and release_date < datetime(2020,8,1):
            return num_reviews * 38
        else:
            return num_reviews * 20
    except:
        print(release_date)

def main():
    #print(reviews_to_sales("18 Apr, 2020", 200000))
    #timestamp_to_date('1607579946')
    pass    

if __name__=='__main__':
    #param = sys.argv[1]
    main()