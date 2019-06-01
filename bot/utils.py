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



def getmovies(msg):
    i,t,type,y=msg.split(',')
    if i=='idk':
        i=""
        if t== "idk":
            datam=dict()
            datam['valid']="0"
            datam['reason']="we need atleast name or id of movie"
            return data
    elif t== 'idk':
        if i == "idk":
            datam=dict()
            datam['valid']=0
            datam['reason']="we need atleast name or id of movie"
            return datam
        else:
            i=""
    elif type == "idk":
        type=""
    elif y == 'idk':
        y=""
    url="http://www.omdbapi.com/?"
    header={"apikey":"omdbapi key","i":i,"t":t,"y":y}
    req=requests.get(url,header)
    datam=req.json()
    return datam
getmovies("idk,avengers endgame,idk,idk")
get_news("in")

