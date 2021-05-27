import json
import pandas as pd
import matplotlib.pyplot as plot

sentiment_file = "Sentimientos.txt"
tweet_records_file = "Tweets.txt"
sentiment_records = open(sentiment_file)

def get_tweets_text(tweet_records_file):
    tweetRecords = open(tweet_records_file)
    key_to_search = "text"
    text_tweets_to_process = []

    for tweet in tweetRecords:
        data = json.loads(tweet)
        if key_to_search in data :
            tweetText = data[key_to_search]
            text_tweets_to_process.append(tweetText)

    return text_tweets_to_process

def calculate_tweets_value(tweets, sentiments_values):
    sentiment_data = []
    for tweet in tweets:
        words_by_tweet = tweet.split()
        associate_sentiment_value = 0
        for word in words_by_tweet:
            if word in values:
                sentimentNumber = sentiments_values[word]
                associate_sentiment_value = associate_sentiment_value + sentimentNumber

        sentiment_data.append([tweet, associate_sentiment_value])

    return sentiment_data

def load_word_values(sentiment_records):
    values = {}
    for record in sentiment_records:
        sentiment, value = record.split("\t")
        values[sentiment] = int(value)

    return values

def calculate_words_without_values(df, sentiments_values):
    values = []
    for record in df:
        tweet_words  = record[0].split()
        value = record[1]
        for word in tweet_words:
            if word not in sentiments_values:
                values.append([record, value, word, value])

    return values


def generate_html(df, page_name):
    text_file = open(page_name, "w")
    text_file.write(df.to_html())
    text_file.close()

values = load_word_values(sentiment_records)

tweets = get_tweets_text(tweet_records_file)

sentiment_data = calculate_tweets_value(tweets, values)

words_without_value = calculate_words_without_values(sentiment_data, values)

#Creando el dataframe para visualizar el sentimiento asociado
sentiment_df = pd.DataFrame(words_without_value, columns = ['Tweet','Sentimiento Asociado','palabra sin valor', 'valor por palabra'])

html = sentiment_df.sort_values('Sentimiento Asociado', ascending=False)

generate_html(html, "palabras_sin_valor.html")

#Creando el dataframe para ver el agrupamiento por valor de sentimiento asociado
#tweet_group = sentiment_df.groupby('Sentimiento Asociado').size().reset_index(name='Cantidad')

#generate_html(tweet_group,"group.html")


