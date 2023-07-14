#!/bin/env python

"""
Scrape an HAR export from Safari Dev Tools
- Open dev tools
- Load a twitter thread
- Scroll to show as many replies as possible
- Click "Export" in the upper right of the network tab
- save as .har file (which is json)
- parse here to scrape all tweet replies
"""

import os.path
import json
import logging
import argparse
from urllib.parse import urlparse

_log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format='%(levelname)s -- %(message)s')


def read_har_replies(fpath):
    with open(fpath, 'r') as f:
        har = json.load(f)

    tweet_replies = []

    for entry in har['log']['entries']:
        url = entry['request']['url']
        parsed_url = urlparse(url)
        resource = os.path.basename(urlparse(url).path)
        if resource == 'TweetDetail':
            tweet_data = json.loads(entry['response']['content']['text'])
            if 'data' in tweet_data and 'threaded_conversation_with_injections_v2' in tweet_data['data']:
                replies = tweet_data['data']['threaded_conversation_with_injections_v2']['instructions'][0]['entries']
                for reply in replies:
                    if 'entryId' in reply and reply['entryId'].startswith('conversationthread-'):
                        result = reply['content']['items'][0]['item']['itemContent']['tweet_results']['result']
                        if 'legacy' in result:
                            reply_text = reply['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['full_text']
                            tweet_replies.append(reply_text)
    return tweet_replies



parser = argparse.ArgumentParser('scrape_har')
parser.add_argument('filename')
args = parser.parse_args()

# _log.info(f"{sys.argv}")

# if len(sys.argv) != 1:
#     _log.error(f"Usage: {sys.argv[0]} <har-file-path>")
#     sys.exit(1)

_log.info(f"Reading {args.filename}")
replies = read_har_replies(args.filename)
_log.info(f"Found {len(replies)} replies in the thread")

out_fpath = args.filename + '.replies.json'
_log.info(f"Writing {out_fpath}")
with open(out_fpath, 'w') as f:
    json.dump(replies, f)
