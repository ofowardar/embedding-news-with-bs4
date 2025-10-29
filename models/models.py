from bs4 import BeautifulSoup
import os
import requests
import json

NEWS_URL = "https://www.hurriyet.com.tr/rss/gundem/"
NEWS_JSON_PATH = "/data/news.json"


# News Class 
class News:
    def __init__(self,news_id,news_content,news_title):
        self.news_id = news_id
        self.news_content = news_content
        self.news_title = news_title



#Soup Class
class Soup:
    def __init__(self,base_url=NEWS_URL):
        self.base_url = base_url

    def take_page(self,path=""):
        response = requests.get(self.base_url + path)
        response.raise_for_status()
        return BeautifulSoup(response.content,"html.parser")
    
    def get_news(self,soup) -> list:
        items = soup.find_all("item")

        news_list = []

        for idx,item in enumerate(items):
            title_tag = item.find("title")           
            description_tag = item.find("description")
            title = title_tag.text if title_tag else "Başlık Yok"
            content = BeautifulSoup(description_tag.text, "html.parser").get_text(strip=True) if description_tag else ""

            news = News(news_id=idx,news_content=content,news_title=title)
            news_list.append(news)

            #test

        return news_list
    
    def return_list_to_json(self,news_list):
        # To Directory
        list_to_dict = [vars(news) for news in news_list ]
        # Dict to JSON
        return json.dumps(list_to_dict,indent=4,ensure_ascii=False)
    
    def write_news_to_jsonf(self, news_json, path="data/news.json"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(news_json)
        print(f"[INFO] JSON dosyası kaydedildi: {path}")
    
    
        


# # Test Block
# soup_obj = Soup()
# all_page = soup_obj.take_page()
# news = soup_obj.get_news(all_page)
# news_json = soup_obj.return_list_to_json(news_list=news)

# # JSON'u ekrana yazdır
# print(news_json)

# # JSON'u dosyaya kaydetmek istersen
# with open("news.json", "w", encoding="utf-8") as f:
#     f.write(news_json)