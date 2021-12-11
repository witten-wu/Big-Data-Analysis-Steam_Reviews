#!/usr/bin/env python

# example: python get_reviews.py 440
# downloads all reviews of a certain game into review_<app_id>.json into folder data

# example: python get_reviews.py
# downloads all reviews for games listed in idlist.txt into folder data

#api key: 580FFF6A399CC261C2340FBC8C1E77C9
import steamreviews
import sys

keys = [
    'recommendationid',
    'language','review',
    'timestamp_created',
    'timestamp_updated',
    'voted_up',
    'votes_up',
    'votes_funny',
    'weighted_vote_score',
    'comment_count',
    'steam_purchase',
    'received_for_free',
    'written_during_early_access']

def get_reviews_id(app_id):
    #app_id = 611760
    request_params = dict()
    #request_params['filter'] = 'recent'
    #request_params['day_range'] = '400'
    review_dict, query_count = steamreviews.download_reviews_for_app_id(app_id, chosen_request_params=request_params, verbose=True)
    #print(review_dict)
    #print(query_count)

def get_reviews_batch():
    steamreviews.download_reviews_for_app_id_batch(verbose=True)

def main(app_id=None):
    if app_id:
        print("Getting reviews of app: {}".format(app_id))
        get_reviews_id(app_id)
    else:
        print("Getting by batch")
        get_reviews_batch()

if __name__=='__main__':
    if len(sys.argv) == 2:
        app_id = sys.argv[1]
        main(app_id)
    else:
        main()