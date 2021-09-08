import json
from bs4 import BeautifulSoup
with open("Task5.json","r")as f:
    data = json.load(f)
def analyse_language_and_directors(data):
    dic={}
    for i in data:
        for j in i["director"]:
            dic[j]={}
    for director in dic:
        for dic_movie in data:
            if director in dic_movie["director"]:
                if "language" in dic_movie:
                    lan=dic_movie["language"]
                    language_Count=0
                    dic[director][lan]=language_Count
                    for each_dict in data:
                        if "language" in each_dict:
                            lan2=each_dict["language"]
                            if (lan==lan2) and director in each_dict["director"]:
                                dic[director][lan]+=1

    with open("Task10.json","w+") as file:
        json.dump(dic,file,indent = 4)
analyse_language_and_directors(data)