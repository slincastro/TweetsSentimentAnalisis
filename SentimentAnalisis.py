import json

sentimentRecords = open("Sentimientos.txt")
tweetRecordsFile = "Tweets.txt"
values = {}

def get_tweets_text(tweet_records_file):
    tweetRecords = open(tweet_records_file)
    key_to_search = "text"
    text_tweets_to_process = []

    for tweet in tweetRecords:
        data = json.loads(tweet)
        if data.has_key(key_to_search) :
            tweetText = data[key_to_search]
            text_tweets_to_process.append(tweetText)

    return text_tweets_to_process

for record in sentimentRecords:
    sentiment, value = record.split("\t")
    values[sentiment] = int(value)

tweets = get_tweets_text(tweetRecordsFile)

for tweet in tweets:
    words_by_tweet = tweet.split()
    value = 0
    for word in words_by_tweet:
        if word in values:
            sentimentNumber = values[word]
            value = value + sentimentNumber

    print("El siguiente tweet : " + tweet + " Tiene un sentimiento asociado de :" + str(value))



