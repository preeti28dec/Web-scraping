import requests
from bs4 import BeautifulSoup
import json
import os
from Task1 import scrape_top_list
from Task4 import scrape_movie_details
movie = scrape_top_list()
def get_movie_list_details():
    movie_list = []
    for i in movie:
        path="/home/dmamatha/Desktop/web/allfiles.txt"+i["Name"]+".text"
        if os.path.exists("file.json"):
            pass
        else:
            create=open(i["Name"]+".text","w")
            url=requests.get(i["Url"])
            create1=create.write(url.text)
            create.close()
            a=scrape_movie_details(i["Name"],i["Url"])
            movie_list.append(a)
        with open("Task5.json","w+") as file5:
            json.dump(movie_list,file5,indent=4)
            print(movie_list)
get_movie_list_details() 