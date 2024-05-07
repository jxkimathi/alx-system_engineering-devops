#!/usr/bin/python3
"""Prints the titles for the first 10 hot posts listed on the Reddit API"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API to find the hot posts"""
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f'https://www.reddit.com/dev/api/r/{subreddit}/hot.json'
    response = requests.get(url, params={"limit": 10}, headers={"User-Agent": 'Custom'})

    if response.status_code == 200:
        for get_data in response.json().get('data').get('children'):
            data = get_data.get('data')
            title = data.get('title')
            print(title)
    else:
        print(None)
