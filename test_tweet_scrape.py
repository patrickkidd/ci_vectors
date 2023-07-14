import requests
from bs4 import BeautifulSoup

def scrape_twitter_thread(thread_url):
    response = requests.get(thread_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    original_tweet = soup.find('div', {'class': 'tweet'})
    print_tweet(original_tweet)

    replies = soup.find_all('div', {'class': 'tweet', 'data-reply-to-users-json': '[]'})

    for reply in replies:
        print_tweet(reply)

def print_tweet(tweet):
    username = tweet.find('span', {'class': 'username'}).text.strip()
    text = tweet.find('div', {'class': 'tweet-text'}).text.strip()

    print(f'Username: {username}')
    print(f'Tweet: {text}')
    print('---')

# Example usage:
thread_url = 'https://twitter.com/jordanbpeterson/status/1679759294428790785'
scrape_twitter_thread(thread_url)
