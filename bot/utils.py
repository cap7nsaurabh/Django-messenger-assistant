import requests
import json
import datetime
import dateutil
import dateutil.parser as datep
def get_help():
    h1 = "this is the following list of commands you can use:\n"
    h2 = "1) !help : get list of commands.\n"
    h3 = "2) !news : get latest news\n"
    h4 = "3) !movie_rating movie_name,movie_release_year : get movie details. name is compulsory and release year \nif  you don't know type 'idk' without space\nuse release year for sequel! example john wick,2019 gives ratings for john wick 3\n"
    return h1+h2+h3+h4
def get_news(cntry):
    key = "your newapi key here" #get yours at https://newsapi.org/
    url = "https://newsapi.org/v2/top-headlines?country=" + str(cntry) + "&apiKey=" + key
    try:
        res = requests.get(url)
    except:
        data={"res":"0","fix":"cannot reach server at the moment, try again."}
        return data
    data = res.json()
    if data["status"] != "ok":
        return "try again" + url + data["status"]
    else:
        return data

def getmovies(msg):
    try:
        t,y=msg.split(',')
    except:
        return "input error please use the format"
    if t== 'idk':
       return "please input atleast name of the movie"
    if y == 'idk':
        y=""
    url="http://www.omdbapi.com/?"
    header={"apikey":"omdb key here","t":t,"y":y} #get you key at http://www.omdbapi.com/
    try:
        req=requests.get(url,header)
    except:
        #datam["res"]="0"
        return "cannot reach server at the moment, try again."
    print(req.json())
    datam = req.json()
    try:
        title="title: "+datam["Title"]+"\n"
        year="Year: "+datam["Year"]+"\n"
        rated="rated: "+datam["Rated"]+"\n"
        release="Release date: "+datam["Released"]+"\n"
        genre="genre: "+datam["Genre"]+"\n"
        ratings1="imdb ratings: "+datam["imdbRating"]+"\n"
        ratings2 = "rotten tomatoes : " + datam["Ratings"][1]["Value"] + "\n"
        ratings3 = "metacritic ratings: " + datam["Ratings"][2]["Value"] + "\n"
        message=title+year+rated+release+genre+ratings1+ratings2+ratings3
    except:
        message="could not fetch data, try again!!check release year and name correctly (if year is unknown type 'idk' instead)"
    return message
def getm(data):
    
def get_cricket_matches():
    key="cric api key here!" # get yours at https://www.cricapi.com/
    url="http://cricapi.com/api/matches"
    header={"apikey":key}
    req=requests.get(url,header)
    li={}
    i=0
    message=""
    data=req.json()
    for item in data['matches']:
        if datep.parse(item['date']).date()==datetime.date.today():
            i=i+1
            st="GM"+str(i)
            li[st]=item
    return li
def extract_message(li):
    message=""
    i=0
    for item in li.values():
        i=i+1
        mes=""
        mes="{}) time:{} gmt\n {} vs {} \n {}\n type GM{} to follow!!\n".format(i,datep.parse(item['dateTimeGMT']).time(),item['team-1'],item['team-2'],item['type'],i-1)
        message=message+mes
        #message="no matches found: retry or there are no matches to follow today"
    return message
