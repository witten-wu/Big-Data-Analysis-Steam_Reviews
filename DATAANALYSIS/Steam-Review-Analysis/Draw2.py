import numpy as np
import pandas as pd
import seaborn
# seaborn.set()
import matplotlib.pyplot as plt
import locale
from locale import atof


Datagame = pd.read_csv('game_info_v2.csv')
DataReview = pd.read_csv('game_reviews_v3.csv')

locale.setlocale(locale.LC_NUMERIC, '')
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
DataAll = Datagame.merge(DataReview, on= 'appId', how='left')

# Draw Fig9
DataAll['hour'].astype(str).str.split(' ',expand=True)
df = pd.DataFrame((x.split(' ') for x in DataAll['hour'].astype(str)),index=DataAll.index,columns=['hours','2','3','4'])
df2 = pd.merge(DataAll,df['hours'],right_index=True,left_index=True)
df2 = df2[df2['hours'] != "#"]
df2['hours'] = df2['hours'].str.replace(',', '').astype(float)
DataFig10 = df2
DataTmp = df2[['name', 'hours']].groupby(['name']).agg('mean')
DataTmp['name'] = DataTmp.index
DataTmp = DataTmp.sort_values(['hours'], ascending=False)
DataTmp = DataTmp.head(n=20)
DataTmp = DataTmp.sort_values(['hours'], ascending=True)
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.barh(y=DataTmp['name'],width=DataTmp["hours"],color="green")
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=15)
plt.title('Average play hours', fontweight="bold")
plt.savefig('Average_play_hours.png',bbox_inches='tight', dpi=300)

# Draw Fig10
DataTmp = DataFig10[['genres0', 'hours']].groupby(['genres0']).agg('mean')
DataTmp['genres0'] = DataTmp.index
DataTmp = DataTmp[DataTmp['genres0'] != "#"]
DataTmp = DataTmp.sort_values(['hours'], ascending=True)
# seaborn.set(style='whitegrid')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.barh(y=DataTmp['genres0'],width=DataTmp["hours"],color="green")
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=15)
plt.title('Average play hours by genres', fontweight="bold")
plt.savefig('Genres_play_hours.png',bbox_inches='tight', dpi=300)

# Draw Fig11
DataTmp1 = DataReview[DataReview['title'] != "Recommended"]
DataTmp2 = DataReview[DataReview['title'] == "Recommended"]
DataTmp2 = DataTmp2.sample(frac=0.2, replace=False)
DataTmp2 = DataTmp2.sort_values(['CLI'], ascending=False)
DataTmp3= DataTmp1[['CLI','Length']].groupby(['CLI'],as_index=False).count() 
DataTmp4= DataTmp2[['CLI','Length']].groupby(['CLI'],as_index=False).count() 
# seaborn.set(style='white')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.plot(DataTmp3['CLI'],(-1)*DataTmp3['Length'],label='Not Recommended',color="red")
plt.plot(DataTmp4['CLI'],DataTmp4['Length'],label='Recommended',color="green")
plt.legend(ncol=1,loc="lower right", frameon=True)
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=15)
plt.ylabel("Num of reviews")
plt.xlabel("CLI")
plt.yticks(range(-500,600,100))
plt.title('Distribution of CLI', fontweight="bold")
plt.savefig('111111.png',bbox_inches='tight', dpi=300)

#Draw 12
# DataTmp1 = DataAll[DataAll['is_free'] ==False]
# DataTmp2 = DataAll[DataAll['is_free'] ==True]
DataTmp= DataAll[['CLI','name']].groupby(['name'],as_index=False).agg("mean")
# seaborn.set(style='white')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.plot(range(1,501,1),DataTmp['CLI'],color="green")
# plt.plot(DataTmp4['name'],(-1)*DataTmp4['CLI'],label='Free',color="red")
# plt.legend(ncol=1,loc="lower right", frameon=True)
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=15)
plt.xlabel("")
plt.ylabel("CLI")
# plt.yticks(range(-1500,2000,500))
plt.title('Average CLI of Games', fontweight="bold")
plt.savefig('22222.png',bbox_inches='tight', dpi=300)

# Draw13
DataTmp1 = DataReview[DataReview['title'] != "Recommended"]
DataTmp2 = DataReview[DataReview['title'] == "Recommended"]
# DataTmp2 = DataTmp2.sample(frac=0.2, replace=False)
# DataTmp2 = DataTmp2.sort_values(['CLI'], ascending=False)
DataTmp3= DataTmp1[['CLI','Length']].groupby(['Length'],as_index=False).count() 
DataTmp4= DataTmp2[['CLI','Length']].groupby(['Length'],as_index=False).count() 
# seaborn.set(style='white')
# seaborn.set(rc={'figure.figsize':(12, 12)})
fig, ax = plt.subplots()
plt.plot(DataTmp3['Length'],(-1)*DataTmp3['CLI'],label='Not Recommended',color="red")
plt.plot(DataTmp4['Length'],DataTmp4['CLI'],label='Recommended',color="green")
# plt.plot(DataTmp3['CLI'],DataTmp3['Length'],label='Not Recommended',color="red")
# plt.plot(DataTmp4['CLI'],DataTmp4['Length'],label='Recommended',color="green")
plt.axhline(y=0, c="k")
plt.vlines(x=(DataTmp3['Length'].median()),ymin=0,ymax=600 ,colors="k")
plt.vlines(x=(DataTmp4['Length'].median()),ymin=-100,ymax=0,colors="k")
plt.legend(ncol=1,loc="upper right", frameon=True)
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=15)
plt.ylabel("Num of reviews")
plt.xlabel("Num of characters")
# plt.yticks(range(-500,600,100))
plt.title('Number of characters per reviews', fontweight="bold")
plt.savefig('333333.png',bbox_inches='tight', dpi=300)

# Draw14
DataTmp1 = DataAll[DataAll['is_free'] ==False]
DataTmp2 = DataAll[DataAll['is_free'] ==True]
DataTmp3= DataTmp1[['CLI','Length']].groupby(['Length'],as_index=False).count() 
DataTmp4= DataTmp2[['CLI','Length']].groupby(['Length'],as_index=False).count() 
fig, ax = plt.subplots()
plt.plot(DataTmp3['Length'],DataTmp3['CLI'],label='Not Free',color="green")
plt.plot(DataTmp4['Length'],(-1)*DataTmp4['CLI'],label='Free',color="red")
plt.axhline(y=0, c="k")
plt.vlines(x=(DataTmp3['Length'].median()),ymin=0,ymax=600 ,colors="k")
plt.vlines(x=(DataTmp4['Length'].median()),ymin=-100,ymax=0,colors="k")
plt.legend(ncol=1,loc="upper right", frameon=True)
plt.ylabel("Num of reviews")
plt.xlabel("Num of characters")
plt.title('Number of characters per reviews', fontweight="bold")
plt.savefig('444444.png',bbox_inches='tight', dpi=300)


#Draw 15
DataTmp= DataAll[['Length','name']].groupby(['name'],as_index=False).agg("mean")
fig, ax = plt.subplots()
plt.plot(range(1,501,1),DataTmp['Length'],color="green")
plt.xlabel("")
plt.ylabel("Num of characters")
plt.title('Average Length of Games', fontweight="bold")
plt.savefig('55555.png',bbox_inches='tight', dpi=300)

#Draw 16
DataTmp= DataAll[['Length','appId']].groupby(['appId'],as_index=False).agg("mean")
DataTmp2 = Datagame.merge(DataTmp, on= 'appId', how='left')
DataTmp2['positive_percentage'] = 100 * (DataTmp2['total_positive'] / DataTmp2['total_reviews']).round(4)
fig, ax = plt.subplots()
plt.plot(DataTmp2['Length'],DataTmp2['positive_percentage'],'ro',color="green",markersize=2)
plt.xlabel("Num of characters")
plt.ylabel("positive_percentage")
plt.title('relationship between length and positive', fontweight="bold")
plt.savefig('666666.png',bbox_inches='tight', dpi=300)

# Draw 17
DataTmp= DataAll[['genres0','Length']].groupby(['genres0'],as_index=False).agg("mean")
DataTmp = DataTmp[DataTmp['genres0'] != "#"]
fig, ax = plt.subplots()
plt.bar(x = DataTmp['genres0'],height = DataTmp['Length'],color="green")
plt.xticks(rotation=90)
plt.ylabel("Num of characters")
plt.title('Average Length by Genres', fontweight="bold")
plt.savefig('777777.png',bbox_inches='tight', dpi=300)

#Draw 18
DataTmp1 = DataAll[DataAll['is_free'] ==False]
DataTmp2 = DataAll[DataAll['is_free'] ==True]
DataTmp3= DataTmp1[['appId','Length']].groupby(['appId'],as_index=False).agg("mean") 
DataTmp4= DataTmp2[['appId','Length']].groupby(['appId'],as_index=False).agg("mean")
DataTmp3= DataTmp3.sample(n=31, replace=False)
fig, ax = plt.subplots()
plt.bar(x = range(1,32,1),height=DataTmp3['Length'],label='Not Free',color="green")
plt.bar(x = range(32,63,1),height=DataTmp4['Length'],label='Free',color="red")
plt.legend(ncol=1,loc="upper right", frameon=True)
plt.ylabel("Average length of reviews")
plt.xticks([])
plt.title('Average Length of Games', fontweight="bold")
plt.savefig('888888.png',bbox_inches='tight', dpi=300)

# Draw 19
DataTmp1 = DataFig10[DataFig10['is_free'] ==False]
DataTmp2 = DataFig10[DataFig10['is_free'] ==True]
DataTmp3= DataTmp1[['appId','hours']].groupby(['appId'],as_index=False).agg("mean") 
DataTmp4= DataTmp2[['appId','hours']].groupby(['appId'],as_index=False).agg("mean")
DataTmp3= DataTmp3.sample(n=31, replace=False)
fig, ax = plt.subplots()
plt.bar(x = range(1,32,1),height=DataTmp3['hours'],label='Not Free',color="green")
plt.bar(x = range(32,63,1),height=DataTmp4['hours'],label='Free',color="red")
plt.legend(ncol=1,loc="upper right", frameon=True)
plt.ylabel("Average play hours of reviews")
plt.xticks([])
plt.title('Average play hours of Games', fontweight="bold")
plt.savefig('999999.png',bbox_inches='tight', dpi=300)


