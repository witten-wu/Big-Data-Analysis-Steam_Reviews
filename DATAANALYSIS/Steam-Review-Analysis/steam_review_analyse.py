import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt


Datagame = pd.read_csv('game_info_v2.csv')
DataReview = pd.read_csv('game_reviews_v3.csv')

DataAll = Datagame.merge(DataReview, on= 'appId', how='left')
#DataAll.to_csv('test.csv', index=False) 

# Draw Fig1
Datagame['total_reviews'] = Datagame['total_reviews'].fillna(0).astype(int)
Datagame['total_positive'] = Datagame['total_positive'].fillna(0).astype(int)
DataTmp = Datagame.sort_values(['total_reviews'], ascending=False)
DataFig1 = DataTmp.head(n=20)
DataFig1 = DataFig1.sort_values(['total_reviews'], ascending=True)
fig,ax = plt.subplots()

plt.barh(y=DataFig1['name'], width=DataFig1['total_reviews'], label='Total Reviews',color="red")
plt.barh(y=DataFig1['name'], width=DataFig1['total_positive'], label='Total Reviews',color="green")
plt.legend(ncol=2,loc="lower right", frameon=True)
plt.title('Most Reviewed Games',fontweight="bold")
plt.savefig('most_reviewed.png', bbox_inches='tight',dpi=300)

# Draw Fig2
Datagame['release_date'].astype(str).str.split(',',expand=True)
df = pd.DataFrame((x.split(',') for x in Datagame['release_date']),index=Datagame.index,columns=['month','year'])
df2 = pd.DataFrame((x.split(' ') for x in df['month']),index=df.index,columns=['date','mon'])
df3 = pd.merge(Datagame,df2,right_index=True,left_index=True)
df4 = pd.merge(df3,df['year'],right_index=True,left_index=True)
DataTmp = df4[['year', 'total_positive','total_reviews']].groupby(['year']).agg('mean')
DataTmp['year'] = DataTmp.index
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.bar(x=DataTmp['year'],height=DataTmp["total_reviews"],label='Avg total Reviews',color="blue")
plt.bar(x=DataTmp['year'],height=DataTmp["total_positive"],label='Avg positive Reviews',color="green")
plt.legend(ncol=2,loc="upper right", frameon=True)
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=15)
plt.xticks(rotation=60)
plt.title('Average reviews by released_year', fontweight="bold")
plt.savefig('release_year_reviews.png',dpi=300)

# Draw Fig3
DataTmp = Datagame[['genres0','total_positive', 'total_reviews']].groupby(['genres0']).agg('mean')
DataTmp['genres0'] = DataTmp.index
DataTmp['positive_percentage'] = 100 * (DataTmp['total_positive'] / DataTmp['total_reviews']).round(4)
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
DataTmp = DataTmp[DataTmp['genres0'] != "#"]
fig, ax = plt.subplots()
#plt.plot(DataTmp['genres0'],DataTmp['positive_percentage'],color='r')
plt.bar(x=DataTmp['genres0'],height=DataTmp["total_reviews"],label='Avg total Reviews',color="blue")
plt.bar(x=DataTmp['genres0'],height=DataTmp["total_positive"],label='Avg positive Reviews',color="green")
plt.legend(ncol=1,loc="upper left", frameon=True)
# plt.bar(x=DataTmp['genres0'],height=DataTmp["total_reviews"],color="green")
# plt.yticks(fontsize=20)
plt.xticks(rotation=90)
plt.title('Average reviews by Genres ', fontweight="bold")
plt.savefig('reviews_by_genres.png',bbox_inches='tight',dpi=300)

# Draw Fig4
Datagame['positive_percentage'] = 100 * (Datagame['total_positive'] / Datagame['total_reviews']).round(4)
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.plot(Datagame['total_reviews'],Datagame["positive_percentage"],'ro',color="green",markersize=2)
# plt.yticks(fontsize=20)
plt.ylabel("positive_percentage")
plt.xlabel("total_reviews")
plt.title('relationship between positive_percentage and total_reviews',fontweight="bold")
plt.savefig('review_and_percentage.png',bbox_inches='tight', dpi=300)

# # Draw Fig5
# Datagame['negative_percentage'] = 100 * (Datagame['total_negative'] / Datagame['total_reviews']).round(4)
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
# fig, ax = plt.subplots()
# plt.plot(Datagame['total_reviews'],Datagame["negative_percentage"],'ro',color="green")
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=15,rotation=90)
# plt.ylabel("negative_percentage",fontsize=25)
# plt.xlabel("total_reviews",fontsize=25)
# plt.title('relationship between negative_percentage and total_reviews',fontsize=25, fontweight="bold")
# plt.savefig('review_and_percentage2.png')

# Draw Fig6
# DataTmp1 = Datagame[Datagame['is_free'] == True]
# DataTmp2 = Datagame[Datagame['is_free'] == False]
# # seaborn.set(style='whitegrid')
# # seaborn.set(rc={'figure.figsize':(12, 12)})
# fig, ax = plt.subplots()
# plt.plot(DataTmp1['total_reviews'],DataTmp1["positive_percentage"],'ro',label='Free games',color="red",markersize=2)
# plt.plot(DataTmp2['total_reviews'],DataTmp2["positive_percentage"],'ro',label='Paid games',color="green",markersize=2)
# plt.legend(ncol=2, loc="lower right", frameon=True)
# # plt.yticks(fontsize=20)
# plt.ylabel("positive_percentage")
# plt.xlabel("total_reviews")
# plt.title('relationship between positive_percentage and total_reviews', fontweight="bold")
# plt.savefig('free_and_paid.png', bbox_inches='tight',dpi=300)

def CLI(text):
    lettercounter = 0
    wordcounter = 0
    sentencecounter = 0
    #checks if the letters are in the alphabet.
    for i in text:
        if (i.isalpha()):
            lettercounter += 1
        # cheks for words
        elif   i == " ":
            wordcounter += 1
        elif i in [".", "!", "?"]:
            sentencecounter += 1
    if wordcounter == 0 and lettercounter != 0:
        wordcounter = 1 
    elif wordcounter == 0:
        return 0
    L = lettercounter * 100 / wordcounter
    S = sentencecounter * 100 / wordcounter
    ColemanLiauIndexScore = round(0.0588 * L - 0.296 * S - 15.8,3)
    if ColemanLiauIndexScore >100:
        ColemanLiauIndexScore = 100
    if ColemanLiauIndexScore < -100:
        ColemanLiauIndexScore = -100
    return ColemanLiauIndexScore

CLIList = []
Comlen = []
for index,row in DataReview.iterrows():
    comment =str(row["comment"])
    CLIList.append(CLI(comment))

for index,row in DataReview.iterrows():
    comment =str(row["comment"])
    Comlen.append(len(comment))

DataReview['CLI'] = CLIList
DataReview['Length'] = Comlen
#DataReview.to_csv('test.csv', index=False) 

y = []
k=0
for index,row in DataReview.iterrows():
    y.append(k)
    k += 1

DataReview['T1'] = y

# # Draw Fig7
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
# fig, ax = plt.subplots()
# plt.plot(DataReview['T1'],DataReview['CLI'],'ro',color="green",markersize=1)
# plt.ylabel("CLI",fontsize=25)
# plt.yticks(fontsize=15)
# plt.title('Distribution of CLI',fontsize=30, fontweight="bold")
# plt.savefig('CLI.png')

# Draw Fig8
DataTmp1 = DataReview[DataReview['title'] != "Recommended"]
DataTmp2 = DataReview[DataReview['title'] == "Recommended"]
DataTmp2 = DataTmp2.sample(frac=0.5, replace=False)
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.plot(DataTmp1['T1'],DataTmp1["CLI"],'ro',label='Not Recommended',color="red",markersize=1)
plt.plot(DataTmp2['T1'],DataTmp2["CLI"],'ro',label='Recommended',color="green",markersize=1)
plt.legend(ncol=1,loc="lower right", frameon=True)
plt.ylabel("CLI")
plt.title('Distribution of CLI',fontweight="bold")
plt.savefig('CLI_Recommend.png',bbox_inches='tight', dpi=300)





