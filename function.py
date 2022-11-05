from ast import keyword
import re
import emoji
import tweepy
from tweepy import Client
import pandas as pd
import re
from matplotlib import pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from dataframe import table
from charting import visualize

def main():
    table()
    visualize()

if __name__ == "__main__":
    main()