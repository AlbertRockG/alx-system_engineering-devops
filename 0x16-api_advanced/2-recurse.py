#!/usr/bin/python3
"""Defines a function that returns a list containing
the titles of all hot articles for a given subreddit.
"""


import requests as rq


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 10
    }
    response = rq.get(
        url=url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results["after"]
    count += results["dist"]
    for child in results["children"]:
        hot_list.append(child["data"]["title"])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
