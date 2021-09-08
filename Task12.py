import json
from bs4 import BeautifulSoup
import requests
movie_url="https://www.rottentomatoes.com/m/toy_story_4"
movie_name="toy_story_4"
def scrape_movie_cast(movie_name,movie_url):
    Url=requests.get(movie_url)
    data=BeautifulSoup(Url.text,"html.parser")
    main_Div=data.find("div",class_="castSection")
    cast_Div= main_Div.find_all("div",class_="media-body")
    dict={}
    list=[]
    for i in cast_Div:
        a=i.span.text
        b=a.strip()
        z=i.find("a",class_="unstyled articleLink")
        dict1={}
        if z!= None:
            c=z["href"]
            s=""
            k=-1
            while k<=len(c[-1]):
                if c[k]=="/":
                    break
                else:
                    s+=c[k]
                k-=1
            a=s[::-1]
            print(a)
            dict1["Name"]=b
            dict1["id"]=a
        else:
            continue       
        list.append(dict1)
    with open("Task12.json","w")as f:
        json.dump(list,f,indent=4)
    return list
scrape_movie_cast("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")