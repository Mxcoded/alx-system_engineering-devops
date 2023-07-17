#!/usr/bin/python3
"""A script that prints the titles of the hottest posts."""
import requests


def top_ten(subreddit):
    """Function that prints the titles of the hottest posts."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = "linux-Moses-Onche/v1.0"

    resp = requests.get(url, params={"limit": 10},
                        headers=header, allow_redirects=False)
    if resp.status_code != 200:
        print("None")
        return
    else:
        data = resp.json()
        for item in data["data"]["children"]:
            print(item['data']['title'])
