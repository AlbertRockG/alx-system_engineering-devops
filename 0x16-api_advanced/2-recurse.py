#!/usr/bin/python3
"""Defines a function that returns a list containing
the titles of all hot articles for a given subreddit.
"""


import requests as rq


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Returns a list of titles of all hot posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "UserAgentAlberTrockG/2.0"}
    params = {"after": after, "count": count, "limit": 100}

    response = rq.get(
        url=url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        for child in results.get("children"):
            hot_list.append(child.get("data").get("title"))
        count += results["dist"]
        after = results.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    return None
