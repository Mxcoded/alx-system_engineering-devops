#!/usr/bin/python3
"""Describes a query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "linux-Moses-Onche/v1.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    resp = requests.get(url, headers=header, params=params,
                        allow_redirects=False)
    if resp.status_code != 200:
        return None
    else:
        data = resp.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for item in results.get("children"):
            hot_list.append(item.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
