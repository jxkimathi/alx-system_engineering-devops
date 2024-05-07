#!/usr/bin/python3
"""Queries the Reddit AI and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Gets number of subscribers after querying the Reddit API"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/dev/r/{subreddit}/about.json'
    user_agent = {'User-agent': 'Custom'}
    response = requests.get(url, headers=user_agent)
    results = response.json()

    try:
        data = results.requests.get('data')
        return data.requests.get('subscribers')

    except Exception:
        return 0
