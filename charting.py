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


def just_tweets(tweets):
    """
    organize the clean tweets in a list
    """
    res = []
    for tweet in tweets:
        res.append(clean_text(tweet.text))
    return res


# source: https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f
def piechart(high, neutral, low):
    sizes = [high, neutral, low]
    ranges = ['Positive', 'Neutral', 'Negative']
    explode = (0, 0.1, 0.1)
    # source: https://www.webucator.com/article/python-color-constants-module/
    colors = ['#00C957', '#FF7F00', '#DC143C']
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=ranges, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')
    ax.set_title("Sentiment Distribution", fontsize=15)
    # plt.pie(pie_chart_list, labels = ranges)
    plt.show()


def volatility_chart(compound_scores):
    plt.plot(compound_scores,
             label="1 = very positive, 0 = neutral, -1 = very negative")
    plt.title("Sentiment Volatilty", fontsize=15)
    plt.xlabel("Days", fontsize=13)
    plt.ylabel("Sentiment Score", fontsize=13)
    plt.grid(True)
    plt.show()


def sentiment_analyzer(result):
    """
    run NLP over the organized tweets to conduct sentiment analysis
    """
    res = []
    compound_scores = []
    num = 0
    high = 0
    neutral = 0
    low = 0
    for tweet in result:
        sentence = result[num]
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        res.append(score)
        compound_scores.append(score['compound'])
        num += 1
    for i in compound_scores:
        if i > 0:
            high += 1
        elif i < 0:
            low += 1
        else:
            neutral += 1
    avg_sentiment = print(
        f'The average sentiment score is: {(sum(compound_scores)/num):.2f}')
    piechart(high, neutral, low)
    volatility_chart(compound_scores)
    return avg_sentiment


def visualize():
    print(sentiment_analyzer(just_tweets(scrape())))


def main():
    visualize()


if __name__ == "__main__":
    main()
