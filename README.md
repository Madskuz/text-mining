# text-mining

To find a twitter ID, use: https://www.codeofaninja.com/tools/find-twitter-id/

Project Overview:

For this project, I used Twitter data (tweets) as a data source in order to analyze the sentiment of X number of the latest tweets by Y user. Sentiment analysis was performed on these tweets using natural language processing (nltk library) in order to derive scores for positive, neutral and negative instances. When approaching this task, I was hoping to be able to deploy a Twitter bot that is able to gauge the overall sentiment of different VC GPs in order to conduct market research and sentiment analysis for my current job.


Implementation:

Since lists are mutable, collecting the text from different tweets and storing it in a list gave me flexibility in removing and adjusting certain elements. It allowed me to pass over my text cleaner function, removing all unnecessary components from the tweets to reduce them to their core text so that I could run an NLP algorithm over it. Eventually, this list of dictionaries (the dictionary being the respective sentiment scores for each tweet) needed to be analyzed. At this point, I had to decide where to keep the data in a dictionary format or extract certain values into a list to analyze. I decided to extract core values from the dictionary and appended them to a list that could be manipulated since it would give me the freedom to build different charts and graphs around the data in the list.

![image](https://user-images.githubusercontent.com/112597537/198938422-3ff04904-980b-4f0b-853f-88e083722df1.png)
Figure 1: Dataframe for key data points on tweets

Results:

After running the sentiment analysis over my last 100 tweets, I found that sentiment typically tends to be highly volatile as pictured in Figure 2. My tweets would jump from close to 1 (highly positive) to 0 (neutral) to close to -1 (highly negative). This is also the case with Babson's Math and Science Twitter account, however, this account has a strong skew toward positive sentiment (see Figure 2). This is an interesting application of sentiment analysis as it can be used to flag an overly negative person on Twitter for review (in case the user is struggling with the likes of depression, etc.).

<img width="587" alt="image" src="https://user-images.githubusercontent.com/112597537/200094822-1fd9581c-d2af-4664-a956-a8153c7e337e.png">
Figure 2: Compound sentiment scores for 100 of my tweets

<img width="584" alt="image" src="https://user-images.githubusercontent.com/112597537/200094854-2219bf30-7480-4c58-a595-b0643eb1adcc.png">
Figure 3: Compound sentiment scores for all of Babson Science and Math Twitter Account (@MathSciBabson) tweets

Another way, I segmented sentiment distribution was by creating 3 classes that separated overwhelmingly positive and negative from more neutral tweets, creating 3 categories in the process, and bucketing tweets into one of the three. Overall, the majority of my tweets (figure 4) are more neutral, while a very small section of my tweets is overwhelmingly negative. Interestingly, I tend to be more neutral than the Babson Twitter account (figure 5), which is likely a function of the Babson twitter serving as a marketing tool and therefore wanting to evoke more positive sentiment. Babson’s twitter average sentiment score (for the last 100 tweets) is 0.35 while mine is 0.23.

<img width="533" alt="image" src="https://user-images.githubusercontent.com/112597537/200094804-22f652d5-e070-4ec1-b6f8-04b83ab404fc.png">
Figure 4: My division of sentiment (positive, negative, neutral) as a proportion of 100 tweets

<img width="513" alt="image" src="https://user-images.githubusercontent.com/112597537/200094846-4d52aeb5-e0dc-408d-b7af-9d1066a62239.png">
Figure 5: @Babson division of sentiment (positive, negative, neutral) as a proportion of 100 tweets

Reflection:

Throughout this process, I learned a lot about web scraping from a social platform and turning the data into actual insight. I was effectively able to build a function sentiment analysis bot that is flexible in the account and number of tweets it analyzes. At its core, it is very simple and there are many ways this could be improved. To begin with, the charts and graphs should be labeled (no title, of axes or numbers on the pie chart) to assist interpretation of the data. Also, my final function (sentiment_analyzer) is way too long and attempts to do too much within one function. Ideally, next time I make more code more concise and neat to prevent this. Going forward, I will be building more in-depth Twitter bots (that notify me when a specific account follows a new account), so I can track new projects that GPs of web 3 VCs are following, allowing me to source more deals in an automated way. To begin with, I found it difficult to navigate through the developer tooling on Twitter's website because none of the example code they gave was in Python. As a result, I wish I had read through a few GitHub repos of different Twitter bots to familiarize myself with the documentation I needed to use (this would have saved time).
