import json
with open("Task5.json","r")as f:
    data = json.load(f)
def analyse_movie_director(data):
    dic1={}
    for i in data:
        for j in i["director"]:
            if j not in dic1.keys():
                c=0
                for z in data:
                    for k in z["director"]:
                        if j==k:
                            c+=1
                dic1[j]=c 
    with open("Task7.json","w+") as director_data:
        json.dump(dic1,director_data,indent = 4) 
analyse_movie_director(data)