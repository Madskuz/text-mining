from ast import keyword
import re
import emoji
import tweepy
from tweepy import Client
import pandas as pd
import re
from matplotlib import pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def input_settings():
    id = input('insert id: ')
    num_tweets = int(input('number of tweets: '))
    return id, num_tweets


def scrape():
    """
    function that allows users to input a Twitter ID and select the number of tweets they want to analyze
    """
    id, num_tweets = input_settings()
    client = tweepy.Client(
        'AAAAAAAAAAAAAAAAAAAAAErvigEAAAAAOasZvHDmIq4wEMbAwRcoQi09ero%3DX66a9NIIaCv88hku9AK3dQV533tm73S3T18BkgXWKMCIhDmFKT')
    # create list to store tweets
    tweets = []
    for tweet in tweepy.Paginator(client.get_users_tweets,  # source for use of paginator: https://github.com/mlachha/Twitter_nlp/blob/main/twitter_bert.ipynb
                                  id=id,
                                  tweet_fields=[
                                      'id', 'created_at', 'public_metrics', 'text', 'source'],
                                  max_results=100).flatten(limit=num_tweets):
        tweets.append(tweet)
    return tweets


def clean_text(txt):  # source: https://python.plainenglish.io/nlp-twitter-sentiment-analysis-using-python-ml-4b4a8fc1e2b
    """
    Create function that cleans the text of the scraped tweets
    """
    txt = re.sub(r"RT[\s]+", "", txt)  # remove retweet (RT)
    txt = txt.replace("\n", " ")  # remove
    txt = txt.replace(" +", " ")
    # source: https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
    txt = re.sub(r"\S*https?:\S*", "", txt)
    txt = re.sub("@[^\s]+", "", txt)  # remove usernames
    txt = txt.replace("#", "")  # remove hashtags
    txt = emoji.replace_emoji(txt, replace='')  # remove emojis
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

def table():
    print(organized_tweets(scrape()))


def main():
    table()


if __name__ == "__main__":
    main()
