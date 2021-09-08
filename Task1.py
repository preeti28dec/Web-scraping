import requests
from bs4 import BeautifulSoup
import json
page = requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
text = BeautifulSoup(page.text,"html.parser")
def scrape_top_list():
    list = []
    div = text.find("div",class_ = "body_main container")
    tbody = div.find("table",class_ = "table")
    tr = tbody.find_all("tr")
    for i in tr:
        dict1 = {}
        td = i.find_all("td")
        for j in td:
            rank = i.find("td",class_ = "bold").get_text()[:-1]
            dict1["Rank"] = int(rank)
            rating = i.find("span",class_ = "tMeterScore").get_text()[1:3]
            dict1["Rating"] = int(rating)
            review = i.find("td",class_ = "right hidden-xs").get_text()
            dict1["Review"] = int(review)
            movieName = i.find("a",class_ = "unstyled articleLink")["href"][3:]
            dict1["Name"] = movieName
            movieurl = i.find("a",class_ = "unstyled articleLink")["href"]
            url = "https://www.rottentomatoes.com" + movieurl
            dict1["Url"] = url
            Year = i.find("a",class_ = "unstyled articleLink").get_text()
            year = Year.strip()
            dict1["Year"] = int(year[-5:-1])
        list.append(dict1)
        if {} in list:
            list.remove({})
    with open("Task1.json","w+") as file:
        json.dump(list,file,indent = 4)
    return list
scrape_top_list()
            