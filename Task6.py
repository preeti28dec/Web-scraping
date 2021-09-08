import json
from bs4 import BeautifulSoup
with open ("Task5.json","r") as f:
    movie=json.load(f)
def Analyse_movie_language(movie):
    language_dic = {}
    for i in movie:
        if "language" in i:
            language = i["language"]
            if language not in language_dic:
                language = i["language"]
                language_dic[language] = 1
            else:
                language_dic[language] += 1
        else:
            continue
    with open("Task6.json","w+") as file6:
        json.dump(language_dic,file6,indent = 4)
Analyse_movie_language(movie)

