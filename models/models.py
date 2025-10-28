from bs4 import BeautifulSoup
import os
import requests
import json

news_url = os.getenv("NEWS_URL")


# News Class 
class News:
    def __init__(self,news_id,news_content,news_title):
        self.news_id = news_id
        self.news_content = news_content
        self.news_title = news_title




#Soup Class
class Soup:
    def __init__(self,base_url=news_url):
        self.base_url = news_url

    def take_page(self,path=""):
        response = requests.get(self.base_url + path)
        response.raise_for_status()
        return BeautifulSoup(response.text,"html.parser")
    
    def get_news(self,soup) -> list:
        articles = soup.find_all("pass","class='pass'")
        news_list = []

        for idx,article in enumerate(articles):
            title = article.find("pass").get_text(strip=True)
            content = article.find("pass").get_text(strip=True)
            news = News(news_id=idx,news_content=content,news_title=title)
            news_list.append(news)
        return news_list
    
    def return_list_to_json(self,news_list):
        # To Directory
        list_to_dict = [vars(news) for news in news_list ]
        # Dict to JSON
        return json.dump(list_to_dict,indent=4,ensure_ascii=False)
    
        


