import json
from bs4 import BeautifulSoup
from Task1 import scrape_top_list
from Task4 import scrape_movie_details
movie = scrape_top_list()
def get_movie_list_details():
    movie_list = []
    for i in movie:
        a = i["Url"]
        list_of_movies = scrape_movie_details(i["Name"],a)
        movie_list.append(list_of_movies)
    with open("Task5.json","w+") as file5:
        json.dump(movie_list,file5,indent = 4)
all_movie_data = get_movie_list_details()

