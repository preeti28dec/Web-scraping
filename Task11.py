import json
with open("Task5.json","r")as file:
    data = json.load(file)
def anlyse_movie_genre():
    i = 0
    list = []
    while i < len(data):
        for key in data[i]:
            if key == "Genre":
                index = 0
                while index < len(data[i][key]):
                    list.append(data[i][key][index])
                    index += 1
        i += 1
    j = 0
    dic = {}
    while j < len(list):
        if list[j] not in dic:
              dic[list[j]] = 1
        else:
            dic[list[j]] += 1
        j += 1
    with open("Task11.json","w")as f:
        json.dump(dic,f,indent = 4)
anlyse_movie_genre()