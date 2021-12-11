#!/usr/bin/env python

#api key: 580FFF6A399CC261C2340FBC8C1E77C9
import json
import requests
import time
import sys

def main():
    with open('idlist.txt', 'r') as f:
        txt = f.read()
    #print(idlist)
    idlist = txt.splitlines()
    
    result = {}
    for id in idlist:
        payload = {'appids': id, 'filters': 'basic,categories,genres,release_date'}
        resp_data = requests.get("https://store.steampowered.com/api/appdetails", params=payload)
        appdetails = resp_data.json()
        #print(appdetails)
        result = {**result, **appdetails}
        time.sleep(0.8)
    with open('appdetails.json', 'w') as f:
        f.write(json.dumps(result))

if __name__=='__main__':
    main()
