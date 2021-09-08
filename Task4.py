import requests
from bs4 import BeautifulSoup
import json
from Task1 import scrape_top_list
movieurl = "https://www.rottentomatoes.com/m/toy_story_4"
movieName = "toy_story_4"
def scrape_movie_details(movieName,movieurl):
    url = requests.get(movieurl)
    data = BeautifulSoup(url.text,"html.parser")
    main_div=data.find_all("li",class_ = "meta-row clearfix")
    dic={}
    for i in main_div:
        x=i.text
        y= x.split(":")
        if "\nRating" in y:
            dic["Rating"] =  y[1].replace("\n","").strip()
        elif "\nGenre" in y:
            gen = y[1].replace("\n                        ","").strip()
            list1 = []
            s = ""
            for i in gen:
                if i == ",":
                    list1.append(s)
                    s = ""
                else:
                    s += i                
            dic["Genre"] = list1
        elif "\nOriginal Language" in y:
            dic["language"] = y[1].replace("\n","").strip()
        elif "\nDirector" in y:
            i = 0
            list2 = []
            while i < len(y):
                if i == 0:
                    i += 1
                    continue
                list2.append(y[i].replace("\n",""))
                i += 1
            add=""
            for s in list2:
                for s2 in s:
                    if s2==" ":
                        continue
                    else:
                        add+=s2
            list5=add.split(",")
            dic["director"]=list5       
        elif "\nProducer" in y:
            i = 0
            list3 = []
            while i < len(y):
                if i == 0:
                    i += 1
                    continue
                list3.append(y[i].replace("\n    ","").strip()) 
                i += 1
                add=""
                for k in list3:
                    for eachch in k:
                        if eachch==" ":
                            continue
                        else:
                            add+=eachch
                list4=add.split(",")
            dic["Producer"] = list4
        elif "\nRuntime" in y:
            s = y[1].replace("\n","").strip()
            h = int(s[0])*60
            i = 0
            j = " "
            while i < len(s):
                if s[i] == "h" or s[i] == "m"  or s[i] == " " or i == 0 or s[i] == "M":
                    i += 1
                    continue
                else:
                    j += s[i]
                    i += 1
                h += int(j)   
            dic["Runtime"] = h
            dic["movieName"] = movieName                   
    with open("Task4.json","w+") as file4:
            json.dump(dic,file4,indent = 4)
            return dic
one_movie_data = scrape_movie_details("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")
                
        
