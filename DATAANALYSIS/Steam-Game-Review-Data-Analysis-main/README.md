To run this project you need Python ver. >= 3.5 as well as the following dependencies:
```
PIL 7.2.0
pandas 1.3
nltk 3.5
requests 2.25.0
scipy 1.5.0
sklearn 0.23.1
seaborn 0.11.0
steamreview 0.9.3
```
wordcloud is another required package that can be found here: https://github.com/amueller/word_cloud.git\
If you only need it for plotting a basic wordcloud, then `pip install wordcloud` or `conda install -c conda-forge wordcloud` will be sufficient. However, the latest version with the ability to mask the cloud into any shape of your choice (as in our project) requires a different method of installation as below:
```
git clone https://github.com/amueller/word_cloud.git
cd word_cloud
pip install .
```

Dataset (big_reviews.csv) can be obtained here: https://www.kaggle.com/najzeko/steam-reviews-2020

### Full Pipeline
```
get_review.py          -> data/review_xxxxx.json
get_applist.py         -> applist.json
get_appdetails.py      -> appdetails.json
make_csv.py            -> big_reviews.csv
steam_analysis_edit.py -> various pngs for visualization
```
