#!/usr/bin/env python

import pandas as pd
import json
import sys
from datetime import datetime

#print(pd.__version__)

# return numpy array representation of dataframe of review_ 
def load_reviews(app_id):
    with open('data/review_{}.json'.format(app_id), 'r') as f:
        data = json.loads(f.read())
    frame = pd.DataFrame.from_dict(data['reviews'], orient='index').reset_index()
    #print(frame.iloc[:, 0:4])
    authordata = pd.json_normalize(frame['author'])
    reviewdata = pd.concat([frame, authordata], axis=1)
    dropped = reviewdata.drop(['author', 'index'], axis=1)
    reviewdata = reviewdata.to_numpy()
    return dropped

# returns dataframe containing 'id' and 'title' based on applist.json
def load_titles():
    titledata = pd.read_json('applist.json', orient='records')
    return titledata

# returns dataframe with various app details as columns (join on the column 'steamp_appid')
def load_appdetails():
    drop = [
        'required_age',
        'controller_support',
        'dlc',
        'detailed_description',
        'about_the_game',
        'short_description',
        'supported_languages',
        'header_image',
        'website',
        'drm_notice', 
        'ext_user_account_notice', 
        'linux_requirements',
        'linux_requirements.recommended',
        'linux_requirements.minimum',
        'mac_requirements',
        'mac_requirements.recommended',
        'mac_requirements.minimum',
        'pc_requirements.recommended',
        'pc_requirements.minimum',
        'legal_notice',
        'release_date.coming_soon',
        'reviews']
    frame = pd.read_json('appdetails.json', orient='index')
    appdetails = pd.json_normalize(frame['data'])
    appdetails['release_date.date'] = appdetails['release_date.date'].apply(json.dumps)
    appdetails['release_date.date'] = appdetails['release_date.date'].apply(lambda x: datetime.strptime(x, '"%d %b, %Y"'))
    dropped = appdetails.drop(drop, axis=1)
    return dropped

def main(app_id=None):
    if app_id:
        print(load_reviews(app_id))
    else:
        #print(load_titles())
        df = load_appdetails()
        print(df.dtypes)
        print(df['release_date.date'])#.iloc[:, 1:4])

if __name__=='__main__':
    if len(sys.argv) == 2:
        app_id = sys.argv[1]
        main(app_id)
    else:
        main()