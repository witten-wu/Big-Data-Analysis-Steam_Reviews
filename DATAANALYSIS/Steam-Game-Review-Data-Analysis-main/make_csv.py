
import pandas as pd
import load

columns = [
    'appid',
    'recommendationid', 
    'language', 
    'review', 
    'timestamp_created', 
    'timestamp_updated', 
    'voted_up', 
    'votes_up', 
    'votes_funny', 
    'weighted_vote_score', 
    'comment_count', 
    'steam_purchase', 
    'received_for_free', 
    'written_during_early_access',      
    #'timestamp_dev_responded',          some (most) review don't have this
    #'developer_response',               some (most) review don't have this
    'steamid', 
    'num_games_owned', 
    'num_reviews', 
    'playtime_forever', 
    'playtime_last_two_weeks', 
    'playtime_at_review', 
    'last_played']

with open('idlist.txt', 'r') as f:
    txt = f.read()
#print(idlist)
idlist = txt.splitlines()
dataframes = []
for id in idlist:
    dataframes.append(load.load_reviews(id))

final = pd.concat(dataframes, ignore_index=True)
final.to_csv('big_reviews.csv')#, header=columns)