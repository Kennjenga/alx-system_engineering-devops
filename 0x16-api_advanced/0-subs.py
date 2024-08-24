#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        except ValueError:
            print("Error: Unable to parse JSON response")
            return 0
    else:
        print(f"Error: Received status code {response.status_code}")
        return 0

