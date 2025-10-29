from bs4 import BeautifulSoup
import os
import requests
import json
from openai import OpenAI

NEWS_URL = "https://www.hurriyet.com.tr/rss/gundem/"
NEWS_JSON_PATH = "/data/news.json"
NEWS_EMBEDDING_PATH = "/data/news_embeded.json"


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
    


class Embedder:
    def __init__(self,model_name="nomic-embed-text:latest",base_url="http://127.0.0.1:11435/v1",api_key="abcd"):
        self.model_name = model_name
        self.base_url = base_url
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key,base_url=self.base_url)

    def embed_text(self,text:str) -> list:
        """
        Sadece 1 adet metni embed eden fonksiyon. Embedding sonucunda matrisi döndürür.
        """

        resp = self.client.embeddings.create(
            input=text,
            model=self.model_name
        )

        return resp.data[0].embedding
    

    def embed_news_list(self,news_list:list) -> list:
        """
        News objelerinin embeddinglerini alır ve her objeye ekler.
        """
        for news in news_list:
            news.embedding = self.embed_text(news.news_content)
        return news_list
    
    def save_embedings(self,news_list,path=NEWS_EMBEDDING_PATH):
        """
        Haberleri Embeddingleri ile birlikte kaydeder. 
        """

        os.makedirs(os.path.dirname(NEWS_EMBEDDING_PATH),exist_ok=True)

        data_to_save = [
            {
                "news_id" : n.news_id,
                "title" : n.news_title,
                "content" : n.news_content,
                "embedding" : n.embedding
            } for n in news_list
        ]

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)
        print(f"[INFO] Embedding JSON kaydedildi: {path}")


        
    
        


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