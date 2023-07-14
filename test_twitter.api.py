import requests
import os

bearer_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

def get_replies(tweet_id):
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "v2GetRepliesPython"
    }

    # Request URL for getting replies to a tweet
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"

    response = requests.get(url, headers=headers)
    response_json = response.json()

    if response.status_code != 200:
        raise Exception(
            f"Cannot retrieve replies (HTTP {response.status_code}): {response_json['errors'][0]['detail']}"
        )

    return response_json["data"]

# Specify the tweet ID for which you want to retrieve replies
tweet_id = "1679759294428790785"

# Get the replies for the specified tweet
replies = get_replies(tweet_id)

# Iterate over the replies and print their text
for reply in replies:
    print(reply["text"])
