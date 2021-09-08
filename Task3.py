import requests
import json
from bs4 import BeautifulSoup
file=open("Task2.json","r")
movies=json.load(file)
def group_by_decade():
    decade_year =[]
    main=[]
    for i in movies:
        year=i
        mod = int(year)%10  #2010%10=0
        decade = int(year)-mod #2010 =2010
        if decade not in decade_year:
            decade_year.append(decade)
        decade_year.sort()    
    movide_dic={}
    index=0
    while index<len(decade_year):
        dec=decade_year[index]+10
        year_list=[]
        for j in movies:
            if int(j)>=decade_year[index] and int(j)<=dec:
                year_list.append(movies[j])
            movide_dic[decade_year[index]]=year_list
        index+=1
    with open("Task3.json","w+") as year_info:
        json.dump(movide_dic, year_info,indent=4)
group_by_decade()


