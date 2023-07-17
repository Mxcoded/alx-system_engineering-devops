#!/usr/bin/python3
"""
Describes a function that gets num of subscribers
in a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Function to query API and return number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "linux-Moses-Onche/1.0"}

    resp = requests.get(url, allow_redirects=False, headers=header)
    if resp.status_code != 200:
        return 0
    else:
        data = resp.json()
        return data['data']['subscribers']
