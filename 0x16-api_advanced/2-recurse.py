#!/usr/bin/python3
"""Recursive function that returns a list containing titles of all hot articles"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursive function that queries the Reddit API for list of titles"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, params={"after": 'after'},
                            headers={"User-Agent": 'Custom'})

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            data = get_data.get("data")
            title = data.get("title")
            hot_list.append(title)
        after = response.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)

    else:
        return None
