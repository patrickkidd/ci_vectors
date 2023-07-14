import json

from transformers import pipeline

def average_opinions(opinions):
    sentiment_analyzer = pipeline("sentiment-analysis")
    
    # Calculate sentiment scores for each opinion
    sentiment_scores = [sentiment_analyzer(opinion)[0]["score"] for opinion in opinions]
    
    # Calculate the average sentiment score
    average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    
    # Determine the polarity label based on the average sentiment score
    if average_sentiment > 0.5:
        polarity = "positive"
    elif average_sentiment < 0.5:
        polarity = "negative"
    else:
        polarity = "neutral"
    
    return polarity

# opinions = [
#     "I think the movie was fantastic!",
#     "In my opinion, the movie was average.",
#     "The movie was terrible, I didn't like it at all."
# ]

REPLIES_FPATH = 'har/musk/1-twitter.com.har.replies.json'
with open(REPLIES_FPATH, 'r') as f:
    opinions = json.load(f)

average_opinion = average_opinions(opinions)
print("The average opinion is:", average_opinion)
