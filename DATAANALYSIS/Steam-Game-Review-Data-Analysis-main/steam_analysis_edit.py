#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from PIL import Image
import scipy.stats as sp
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk # Natural Language ToolKit
nltk.download('stopwords')
import seaborn
seaborn.set()
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")   # for transparency issues regarding wordcloud masking image
from transform import *
from load import *

#Loading the data
df = pd.read_csv('big_reviews.csv')
print("Main data loaded")

df_frame = load_titles()
df = df.merge(df_frame)

# ------------1. Word Cloud Generation---------------- #

#df_positive = df[df['voted_up'].isin(['True'])]
df_positive = df[df['voted_up'] == True]
#df_positive = df_positive.filter(df_positive['language'] == 'english')
df_wc_positive = df_positive[df_positive['language'] == 'english']
#df_positive = df_positive[df_positive['language'] == 'english']

# Converting the list to string
text = ' '.join(str(line).strip() for line in df_wc_positive.review)
print("There are {} words in the combination of all reviews.\n".format(len(text)))

# Using the NLTK library of stopwords and adding new stopwords
# (Stopwords: words to be filtered out)
stop_words = set(nltk.corpus.stopwords.words('english'))

my_stop_words = ['time', 'game', 'free', 'product', 'people', 'finish', 'great', 'amazing', 'really',
                 'better', 'best', 'start', 'now', 'find', 'fun', 'still', 'in', 'cool', 'long', 
                 'go', 'work', 'run', 'say', 'even', 'gt', 'one', 'seems', 'everyone', 'see', 'need', 
                 'thing', 'much', 'take', 'never', 'want', 'will', 'well', 'far', 'look', 'pretty',
                 'always', 'got', 'made', 'think', 'way', 'problem', 'feel', 'well', 'going', 'little',
                 'guy', 'said', 'everything', 'thing', 'know', 'access', 'something', 'received', 
                 'now', 'product', 'play', 'friend', 'best', 'get', 'love', 'like', 'Steam', 'there', 
                 'favorite', 'favourite', 'awesome', 'great', 'excellent', 'though', 'through', 'put', 
                 'finish', 'playing', 'nice', 'recommend', 'first', 'would', 'every', 'good', 'I\'m',
                 'buy', 'make', 'played', 'bug', 'need', 'lot', 'give', 'back', 'lot', 'review', 'also',
                 'could', 'keep', 'hard', 'dont', 'don\'t', 'about', 'many', 'try', 'I\'ve', 'day',
                 'right', 'can\'t', 'thing', 'around', 'worth', 'bit', 'enjoy', 'come', 'Ye', 'die', 'bad',
                 'ever', 'that', 'year', 'getting', 'since', 'enough', 'stuff', 'early', 'yet', 'however',
                 'because', 'actually', 'use', 'someone', 'sure', 'fix', 'thing', 'sometime', 'alot',
                 'pre', 'high', 'fp', 'fps', 'im', 'bug', 'fixed', 'hour', 'player', 'anyone', 'wait', 
                 'issue', 'already','rust', 'Yes', 'makes', 'lots', 'games', 'issues', 'hours', 'sometimes', 
                 'needs', 'overall', 'gets', 'u', 'open', 'let', 'bugs', 'without', 'highly', 'full', 
                 'things', 'big', 'nothing', 'everything', 'none', 'naked', 'PUBG', 'minute', 'ing', 
                 'quite', 'two', 'please', 'V', 'looking', 'old', 'ball', 'another', 'version', 'lag', 
                 'especially', 'point', 'lt', 'add', 'part', 'end', 'person', 'help', 'definitely', 
                 'almost', 'cant', 'dev', 'must', 'bought', 'years', 'last', 'probably', 'stop', 'devs', 
                 'able', 'may', 'base', 'running', 'killed', 'killing', 'match', 'making', 'times', 
                 'trying', 'problems']

stop_words.update(my_stop_words)

# Generate a word cloud with the data and stopwords:
wordcloud = WordCloud(max_words=70, width=3000, height=2000, colormap='coolwarm',
                     collocations=False, stopwords=stop_words).generate(text)

#Save it to file
wordcloud.to_file("wordcloud.png")


# Alternative visualisation:
# Word cloud from Steam logo shape and colour

# Load Steam logo
logo = np.array(Image.open('steam_blue.png'))

# Transform all the (white) pixels with value 0 to value 255
def transform_logo(val):
    if val == 0:
       return 255
    else:
       return val

# Use the function to generate a mask for the word cloud
new_logo = np.ndarray((logo.shape[0], logo.shape[1]), np.int32)

for i in range(len(logo)):
    new_logo[i] = list(map(transform_logo, logo[i]))

wordcloud_alt = WordCloud(max_words=70, width=2400, height=2398,
                      background_color='white', mask=new_logo, mode='RGBA',
                      collocations=False, stopwords=stop_words).generate(text)
rgb_logo = np.array(Image.open('steam_blue.png').convert('RGB'))
image_colors = ImageColorGenerator(rgb_logo)
plt.figure(figsize=[7,7])
plt.imshow(wordcloud_alt.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis('off')
plt.savefig('steam_coloured_cloud.png')


# ------------2. Positive Percentage Analysis---------------- #

# Add column 'year' and 'month' derived from 'date_posted'
df['datereview'] = df['timestamp_created'].astype(int)

df['datereview'] = timestamp_to_date(df['datereview'])

df['year'] = df['datereview'].astype(str).str[0:4].astype(int)
df['month'] = df['datereview'].astype(str).str[5:7].astype(int)
df['year_month'] = df['datereview'].astype(str).str[0:7]


reviews = df[['year_month', 'review']].groupby(['year_month']).agg('count')
reviews['year_month'] = reviews.index    # After groupby, year_month becomes index; reset it to column

#seaborn.set(font_scale=0.8)
ax = seaborn.barplot(x='year_month', y='review', data=reviews)
ax.set_xlabel("Time")
ax.set_ylabel("Number of reviews")

# Avoid the compaction of time periods shown
# Every 5th label is shown
for ind, label in enumerate(ax.get_xticklabels()):
    label.set_rotation(45)
    if ind % 50 == 0:
        label.set_visible(True)
    else:
        label.set_visible(False)

plt.savefig('num_total_reviews.png')


# What are the best-rated games (i.e. having the biggest number of positive reviews)
# .. from 2013 to 2016?
# (fewer reviews in this period, so counted together)
df_13_16 = df[(df['voted_up'] == True)     & ((df['year'] == 2013) | (df['year'] == 2014)     | (df['year'] == 2015) | (df['year'] == 2016))]
df_13_16_count = df_13_16[['name','review']].groupby('name').count()     .sort_values(['review'], ascending=False)
df_13_16_count = df_13_16_count.rename(columns={'review': 'positive_review'})
print('---*** Best rated games from 2013 to 2016 ***---')
print(df_13_16_count.head(n=5).to_string())

df_17 = df[(df['voted_up'] == True) & (df['year'] == 2017)]
df_17_count = df_17[['name','review']].groupby('name').count()     .sort_values(['review'], ascending=False)
df_17_count = df_17_count.rename(columns={'review': 'positive_review'})
print('\n\n---*** Best rated games in 2017 ***--- ')
print(df_17_count.head(n=5).to_string())

# ... from 2018 to 2019 (data up to Feb 2019)?
df_18_19 = df[(df['voted_up'] == True)     & ((df['year'] == 2018) | (df['year'] == 2019))]
df_18_19_count = df_18_19[['name','review']].groupby('name').count()     .sort_values(['review'], ascending=False)
df_18_19_count = df_18_19_count.rename(columns={'review': 'positive_review'})
print('\n\n---*** Best rated games from 2018 to Feb 2019 ***---')
print(df_18_19_count.head(n=5).to_string())

# What game has the biggest number of reviews of all time, across all categories?
count_total_revs = df[['name','review']].groupby('name').count()     .sort_values(['review'], ascending=False)
count_total_revs.rename(columns={'review': 'total_review'}, inplace=True)

# ... POSITIVE reviews of all time?
count_pos_revs = df_positive[['name','review']].groupby('name').count()     .sort_values(['review'], ascending=False)
count_pos_revs.rename(columns={'review': 'positive_review'}, inplace=True)

# Join and calculate the percentage
rev_counts = count_total_revs.join(count_pos_revs, how='left')
rev_counts['positive_review'] = rev_counts['positive_review'].fillna(0).astype(int)
rev_counts['positive_percentage'] = 100 * (rev_counts['positive_review'] / rev_counts['total_review']).round(4)

print('---*** Ten most reviewed games for offically all time ***---\n')
rev_counts_head = rev_counts.head(n=10)
print(rev_counts_head.to_string())

rev_counts_head.reset_index(level=0, inplace=True)

# Visualisation
seaborn.set(style='whitegrid')
seaborn.set(rc={'figure.figsize':(12, 5)})
fig, ax = plt.subplots()

# Plot total reviews
seaborn.set_color_codes('pastel')
seaborn.barplot(x='total_review', y='name', data=rev_counts_head,
            label='Total Reviews', palette='Blues_r')

# Remove label
ax.set_ylabel('')    

# Plot positive reviews
seaborn.set_color_codes('muted')
seaborn.barplot(x='positive_review', y='name', data=rev_counts_head,
            label='Positive Reviews', palette='bone')

ax.set_ylabel('')

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlabel='Ten Most Reviewed Games from Dataset')
seaborn.despine(left=True, bottom=True)
plt.savefig('ten_most_reviewed.png', bbox_inches='tight')


# TODO: replace this with the true number of sales
appdetails = load_appdetails()
rev_counts = rev_counts.join(appdetails)
rev_counts['sales'] = rev_counts.apply(lambda x: reviews_to_sales(x['release_date.date'], x['total_review']), axis=1)
print(rev_counts)
rev_corr = rev_counts

# Filter out games with less than 100 reviews
rev_corr = rev_corr[rev_corr['total_review'] >= 200]

# Filter out games with 100% good reviews
rev_corr = rev_corr[rev_corr['positive_percentage'] != 100]

# Calculate correlation coefficient:
correlation = rev_corr['positive_percentage'].corr(rev_corr['sales'])
print('Correlation between the percentage of positive reviews and a game\'s sales: {:.2f}.\n'.format(correlation))

# Or a linear regression:
fit = sp.linregress(rev_corr['sales'], rev_corr['positive_percentage'])
rev_corr['positivity_regress'] = rev_corr['sales']*fit.slope + fit.intercept

# Check residuals
rev_corr['residuals'] = abs(rev_corr['positive_percentage'] - rev_corr['positivity_regress'])
seaborn.displot(rev_corr, x='residuals', bins=15, color='black')
plt.savefig('residuals_of_linreg.png')

print('P-value of linear regression: {}\n\n'.format(fit.pvalue))

# Visualise the scatterplots and linear regression line:
g = seaborn.jointplot(x='sales', y='positive_percentage', data=rev_corr, kind='reg', color='green', height=6)
g.fig.suptitle('Correlation Between Game Sales and Positivity of Reviews')
g.set_axis_labels('Sales', '% of positive reviews', fontsize=14)

plt.savefig('sales_posrev_corr.png')



# ------------3. Hours Played v.s. Review Positivity---------------- #

# Visualise hours played before players leave a review
# Using a distribution plot
seaborn.set(style='whitegrid')
seaborn.distplot(df['playtime_at_review'], bins=20,
                hist_kws={'linewidth': 3, 'alpha': 1, 'color': 'g', 'label': 'Hours played'})
plt.xlabel('')
plt.legend()
plt.title('Distribution of Hours Played Before Leaving a Review')
plt.savefig('hours_before_rev.png')

# Data is right-skewed
# Create another displot of range to 0-1000
df_filt = df[(df['playtime_at_review'] <= 1000)]
seaborn.set(style='whitegrid')
seaborn.distplot(df_filt['playtime_at_review'], bins=20,
                hist_kws={'linewidth': 3, 'alpha': 1, 'color': 'g', 'label': 'Hours played'})
plt.xlabel('')
plt.title('Distribution of Hours Played Before Leaving a Review (Showing up to 1000)')
plt.legend()
plt.savefig('hours_before_rev_up_to_1000.png')

print(df['playtime_at_review'].describe().round(2))

# Bin reviews into 100 divisions based on hours_played, representing percentage
df['hour_category'] = pd.Series(pd.qcut(df['playtime_at_review'], q=500, duplicates='drop'))

# Group by these categories, calculate the rate of positive comments
total_size = df.groupby('hour_category').size()
positive_size = df[df['voted_up'] == True].groupby('hour_category').size()
pos_time = pd.DataFrame(positive_size/total_size, columns=['positivity']).reset_index()
#pos_time = pos_time.applymap(float)

# Approach 1: Time Interval Category as x-axis
# Which means hours played quantized by number of players

seaborn.set(style='whitegrid')
seaborn.relplot(x=pos_time['hour_category'].cat.codes.values, y='positivity', data=pos_time, palette='Blues')
plt.xlabel('Hours Played Before Review (Quantized Percentage)')
plt.ylabel('Rate of Positive Reviews')
plt.savefig('positivity_by_hours_quantized.png', bbox_inches='tight')

# Approach 2: Midpoint of time intervals as x-axis
# Without quantization

# Find the mid point of each time interval
# And cast it as type float
pos_time['hour_mid'] = pos_time['hour_category'].apply(lambda x: x.mid)
pos_time['hour_mid'] = pos_time.hour_mid.astype(str).astype(float)

# Visualise data
seaborn.set(style='whitegrid')
seaborn.relplot(x='hour_mid', y='positivity', data=pos_time, color='blue', alpha=0.6)
plt.xlim(0, 1500)
plt.xlabel('Number of Hours Played, in Real Time')
plt.ylabel('Rate of Positive Reviews')
plt.savefig('positivity_by_hours_real.png', bbox_inches='tight')


# Then use a polynomial regressor to fit data
# Using Time Interval Categories (i.e. approach 1)

# Define input and output
# For input: Turn categorical data into integers, and reshape into 2D array
X = pos_time['hour_category'].cat.codes.values.reshape(-1, 1)
y = pos_time['positivity'].values

# Split into train and test sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

# Fit the model (with scaling first)
model = make_pipeline(
    MinMaxScaler(),
    PolynomialFeatures(degree=12, include_bias=True),
    LinearRegression(fit_intercept=False)
)
model.fit(X_train, y_train)
print('Fitting a 12th-degree polynomial regressor to the data\nValidation Score: %.5g' % (model.score(X_valid, y_valid)))


# Plot the data
seaborn.set(style='whitegrid')
seaborn.relplot(x=pos_time['hour_category'].cat.codes.values, y='positivity', data=pos_time[['hour_category', 'positivity']], palette='Blues', alpha=0.7, legend=False)
plt.xlabel('Hours Played Before Review (Quantized Percentage)')
plt.ylabel('Probability of Leaving a Positive Review')

plt.plot(X, model.predict(X), color='green', linewidth='3', alpha=0.8)

plt.axis('tight')
plt.title('Relationship Between Hours Played and Positively Reviewing')

plt.savefig('pos_hours_poly_fit.png', bbox_inches='tight')

