from models.models import Soup, Embedder, News
import warnings
warnings.filterwarnings("ignore")
from models.similarity import search_news
from pathlib import Path
import json

embeded_path = "C:/Users/Ömer Faruk Özvardar/Desktop/Makine Öğrenimi Ödev/data/embedded.json"
normal_news_path = "C:/Users/Ömer Faruk Özvardar/Desktop/Makine Öğrenimi Ödev/data/news.json"

# ---------------------------- Scrapping and Saving to file.
if not Path(normal_news_path).exists():
    soup = Soup()
    all_page = soup.take_page()
    news_list = soup.get_news(all_page)
    news_json = soup.return_list_to_json(news_list=news_list)
    soup.write_news_to_jsonf(news_json, path=normal_news_path)
else:
    with open(normal_news_path, "r", encoding="utf-8") as f:
        news_list_dict = json.load(f)
    news_list = [News(**item) for item in news_list_dict]

# ---------------------------- Embedding and take similarity.
embedder = Embedder()
if not Path(embeded_path).exists():
    news_with_embedding = embedder.embed_news_list(news_list)
    embedder.save_embedings(news_with_embedding, path=embeded_path)
else:
    with open(embeded_path, "r", encoding="utf-8") as f:
        embedded_list = json.load(f)
    for news, emb_dict in zip(news_list, embedded_list):
        news.embedding = emb_dict["embedding"]
    news_with_embedding = news_list

# ---------------------------- Similarity and Search News
user_query = input("Lütfen Aramak İstediğiniz Haberi Giriniz: ")
top_news = search_news(query=user_query, news_list=news_with_embedding, embedder=embedder, top_k=4)

# See the Results...
for score, news in top_news:
    print(f"[{score:.3f}] {news.news_title}")
