from ast import keyword
import nltk
import re
import emoji
import tweepy
import config
from tweepy import Client
import pandas as pd
import re
import json
import matplotlib

def scrape():
    """
    function that allows users to input a Twitter ID and select the number of tweets they want to analyze
    """
    id = input('insert id: ') # source: https://developer.twitter.com/en/portal/products/elevated
    num_tweets = int(input('number of tweets: '))
    client = tweepy.Client('INSERT_BEARER_TOKEN_HERE')
    # create list to store tweets
    tweets = []
    for tweet in tweepy.Paginator(client.get_users_tweets, # source for use of paginator: https://github.com/mlachha/Twitter_nlp/blob/main/twitter_bert.ipynb
                                    id = id,
                                    tweet_fields = ['id','created_at', 'public_metrics', 'text', 'source'], 
                                    max_results=100).flatten(limit = num_tweets):
        tweets.append(tweet)
    return tweets


def clean_text(txt): # source: https://python.plainenglish.io/nlp-twitter-sentiment-analysis-using-python-ml-4b4a8fc1e2b
    """
    Create function that cleans the text of the scraped tweets
    """
    txt = re.sub(r"RT[\s]+", "", txt) # remove retweet (RT)
    txt = txt.replace("\n", " ") # remove
    txt = txt.replace(" +", " ")
    txt = re.sub(r"\S*https?:\S*", "", txt) # source: https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
    txt = re.sub("@[^\s]+", "", txt) # remove usernames
    txt = txt.replace("#", "") # remove hashtags
    txt = emoji.replace_emoji(txt, replace='') # remove emojis
    txt.strip()
    return txt

def sentiment_analyzer(txt):
    """
    create a sentiment analyzer for the tweets
    """
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sentence = txt
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score

def organized_tweets(tweets):
    """
    organize the clean tweets in a dataframe
    """
    res = []
    for tweet in tweets:
        res.append({'cleaned_text': clean_text(tweet.text),
                        'likes': tweet.public_metrics['like_count'],
                        'retweets': tweet.public_metrics['retweet_count'],
                        'sentiment': sentiment_analyzer(tweet.text) 
                        })
    df = pd.DataFrame(res)
    return df

print(organized_tweets(scrape()))

def just_tweets(tweets):
    """
    organize the clean tweets in a dataframe
    """
    res = []
    for tweet in tweets:
        res.append(clean_text(tweet.text))
    return res

def sentiment_analyzer(res):
    """
    run NLP over the organized tweets to conduct sentiment analysis
    """
    from matplotlib import pyplot as plt
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    res2 = []
    compound_scores = []
    num = 0
    high = 0
    middle = 0
    low = 0
    for tweet in res:
        sentence = res[num]
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        res2.append(score)
        compound_scores.append(score['compound'])
        num += 1
    for i in compound_scores:
        if i > 0.5:
            high += 1
        elif i < -0.5:
            low += 1
        else:
            middle += 1
    pie_chart_list = [high, middle, low]
    ranges = ['Positive', 'More Neutral', 'Negative']
    fig = plt.figure(figsize =(10,7))
    plt.pie(pie_chart_list, labels = ranges)
    plt.show()
    avg_sentiment = print(f'The average sentiment score is: {(sum(compound_scores)/num):.2f}')
    plt.plot(compound_scores)
    plt.show()
    return res2, avg_sentiment

sentiment_analyzer(just_tweets(scrape()))
