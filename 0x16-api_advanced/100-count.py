#!/usr/bin/python3
"""Defines a function to count words in all hot
posts of a given Reddit subreddit."""


import requests as rq


def count_words(subreddit, word_list, dict_of_words=None, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        dict_of_words (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = rq.get(
        url=url,
        headers=headers,
        params=params,
        allow_redirects=False
        )
    if dict_of_words is None:
        dict_of_words = dict()
        for word in word_list:
            lowercase_word = word.lower()
            if not (dict_of_words.get(lowercase_word)):
                dict_of_words[lowercase_word] = 0

    if response.status_code == 200:
        data = response.json().get("data")
        for child in data["children"]:
            title = child["data"]["title"].lower().split()
            for i in range(len(title)):
                for word in word_list:
                    if title[i].lower() == word.lower():
                        dict_of_words[word.lower()] += title.count(
                            word.lower()
                            )

        count += data["dist"]
        after = data["after"]
        if after is not None:
            return count_words(
                subreddit,
                word_list,
                dict_of_words,
                after, count
                )
        if len(dict_of_words) == 0:
            print("")
            return
        dict_of_words = sorted(
                dict_of_words.items(),
                key=lambda kv: (-kv[1], kv[0])
                )
        [print("{}: {}".format(k, v)) for k, v in dict_of_words if v != 0]

    if response.status_code != 200:
        return
