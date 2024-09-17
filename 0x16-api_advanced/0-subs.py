#!/usr/bin/python3
"""Queries the Reddit API and returns
the number of subscribers (not active
users, total subscribers) for a given
subreddit. If an invalid subreddit is
given, the function should return 0.
"""

import requests as rq


def number_of_subscribers(subreddit):
    """Get the total number of subscribers
    for a given subreddit. If not a valid
    subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent/0.1'}
    response = rq.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get('subscribers', 0)
    else:
        return 0
