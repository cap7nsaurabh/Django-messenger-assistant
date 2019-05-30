import requests
import json


def get_news(cntry):
    key = "get yours at newsapi"
    url = "https://newsapi.org/v2/top-headlines?country=" + str(cntry) + "&apiKey=" + key
    res = requests.get(url)
    data = res.json()
    if data["status"] != "ok":
        return "try again" + url + data["status"]
    else:
        return data




