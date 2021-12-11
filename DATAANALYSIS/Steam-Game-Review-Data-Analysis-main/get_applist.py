#!/usr/bin/env python

#api key: 580FFF6A399CC261C2340FBC8C1E77C9
import requests
import json
import sys


def main():
    with open('idlist.txt', 'r') as f:
        txt = f.read()
    #print(idlist)
    idlist = txt.splitlines()
    idset = set(idlist)
    print(idset)

    resp_data = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    applist = resp_data.json()
    applist = applist['applist']['apps']
    #print(applist['applist']['apps'])
    idfiltered = [x for x in applist if str(x['appid']) in idset]
    print(idfiltered)
    with open('applist.json', 'w') as f:
        f.write(json.dumps(idfiltered))

if __name__=='__main__':
    main()