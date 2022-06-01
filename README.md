### Big-Data-Analysis-Steam_Reviews

### Abstract
With the development of game industry, digital distribution platform for gaming is popular in the 21st century. As one of the largest-scale online vendors, steam has more than 34,000 games and approximately 100 million of active users. Review system is a unique community in steam, on which the content of reviews is a significant reference for potential buyers to make decisions. Hence, study on game reviews is able to provide game developer an improvement direction and a more comprehensive understanding of players' concern. This project aims to complete a visualization and further analysis on review captured from steam by some big data processing tools, and try to conclude some real-world impact as well as some possible suggestions to game developers.

### Introduction
With the higher spiritual requirements of people in the 21st century, game industry developed with rapid speed are of high revenue. As a video game digital distribution service by Valve, STEAM has been the largest digital distribution platform for PC gaming with nearly 34000 games.
In addition to video game digital distribution service, Steam also has a unique community system containing official and folk content related to its games, and Steam reviews is the most important part of steam community. Most games served on steam allow reviews posted from purchaser, which gradu- ally becomes an important reference for potential buyers to make their decision.
In this project, we captured totally 100,000 reviews on top 500 most popular games from steam platform. And we aimed to perform a study on the visual- ization and analysis of the reviews by big-data analyzing methods learned from this course, to try to explore some conclusions and real-world impacts on steam reviews.

<img width="564" alt="image" src="https://user-images.githubusercontent.com/38986230/171348427-0105c097-872a-426a-bba2-fc58f78ba350.png">

### Motivation
As mentioned before, review content plays a significant role for potential buyers as reference. Meanwhile, the overall trend of reviews of a game will have a strong effect on sales and downloads. Hence, study on the constitution of reviews could help game developer better understand the thought from players, furtherly help them on the development directions. In addition, as we know the potential buyers will refer to the content of negative comments rather than positive ones, the study we made on our project wants to help game developer find a better way to improve the game quality by exploring some methods to reduce the appearance of negative reviews.

### Objective
The aim of the project is to perform a study and analysis on the steam review data, as well as to have a better understanding of the roles of big-data processing tools like MapReduce studied in this course.

### Dataset preparation
A review of a game is player's evaluation for the game itself, and may also be:
A little thought about the game 
Disagreement on shortcomings 
Thanks for the wonderful experience 
Feedback on game bugs
Important reference to judge whether a game is worth buying/playing
···
Huge reviews data on Steam is a valuable information library. But reviews
of a certain game usually focus on the game itself. In order to discover more useful information from steam reviews, we selected 500 games, each with 200 reviews, 100,000 reviews in total to analyze reviews as a whole.
We choose top 500 global top sellers on Steam store and get a game list with 500 games, note that this game list does not include game that is not yet available and the number of reviews is less than 200.
Steam provides an official API to get game information:
get https://store.steampowered.com/api/appdetails/?appids={appid}

### Methodology
#### Hadoop Distributed computing
The Apache Hadoop is a framework where massive amounts of data is able to store by distributed nodes. Because the computing and storage functions are implemented by the collections of nodes or machines which have their own resources, processing of large data sets is allowed to be handled and even opti- mized by parallel computing of each node.

#### MapReduce
As we know, MapReduce is a software framework for parallel computing and execution. It provides a large but well-designed parallel computing software framework, which can automatically complete the parallelization of computing tasks, automatically divide computing data and computing tasks, automatically assign and execute tasks on cluster nodes and collect computing results. The system is responsible for processing many complex details of the bottom of the system involved in parallel computing, such as data distribution storage, data communication, fault tolerance processing, which greatly reduces the burden of software developers.

#### Parallel Computing in Python
A simple data preprocessing is required before further work to drop the re- dundant columns in raw .csv file. The purpose of this step is also useful to simplify the script of Pig Latin and improve the load time in Hadoop. Mean- while, changing the format of data and generating new column are integral before loading them into Pig Latin.
Parallel computing is a more time-saving work rather than serial computing on the computer having multiple Central Processing Units (CPU) to solve a computational problem. And pandas in Python is a powerful, fexible and easy to handle .csv file open-source data analysis tool, so we chose Python parallel computing to process this task.
In this steam data analysis project, our target is to calculate the word count and re-generate the correct data type of playtime (in hours) of each review stored by a .csv file. Obviously, this problem is able to be broken into discrete parts that can be solved concurrently.

#### Pig Latin Query
As we know, Hadoop architecture is able to process data transformation and aggregation by parallel manner. However, rather than hundreds of lines in traditional MapReduce implemented by Java API, Apache Pig is a more convenient and less complex language for analyzing this dataset.
The Pig Latin Queries is a SQL-like command, which is suitable for the playtime-based analysis in our project. We have written the Pig queries to find out the correlation between playtime and other features of each review on several conditions. Totally 3 pairs of comparison and corresponding 6 Pig Latin queries are designed to generate the data for further visualization. To make the result more real-word related, we aim to compare playtime between positive and negative review, free-to-play and not free-to play games, and the review length in two kinds of attitudes.

### Discussion
Most games receive reviews with a relatively short length and high readabil- ity. This points the way for further analysis of game reviews. More advanced review selection and summarization techniques are needed for developers with the most reviews, or for developers who cannot go through their daily reviews for other reasons, which will also improve and evolve the content and quality of the game.
We calculated the median of negative reviews for all games is 34, which means more than half of 'Not Recommended' comments are posted during this time duration.
Based on the commenting rules on steam, each player could only leave the comment only once on each game. Hence, it could be suggested that the game designer should show the most excellent part and as much as freshness in the first 34 hours to lead players to post a positive review, which could be one design orientation to reduce rate of bad reviews.
Another interesting discovery is there existed an obvious density peak at the time of first hour on both free-to-play and not free- to-play games. It could be imagined that many players who are not satisfied with the game content post a negative review and leave the game soon after 1-hour boring gaming. So, another advise we found from the visualization is that the gameplay experience in the first hour is the most important for the game designer to attract the players.

### Conclusion
Study and analysis of Steam reviews is an interesting topic. From the study of this project, we understand that big data analyzing on comments by users is able to help game developers as well as service vendors know about users' concerns, and help improve game quality. Big data of Steam reviews could even play an important role for giants on game industry to predict market trends on user preferences, which regrettably not covered on this project due to time and ability limits. Game review analysis is meaningful in several aspects and this project is indeed a comprehensive exploration of big data knowledge for us.
