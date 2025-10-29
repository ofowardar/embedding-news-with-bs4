from models.models import Soup,Embedder
import warnings
warnings.filterwarnings("ignore")




# ---------------------------- Scrapping and Saving to file.

# Create a Soup() object
soup = Soup()

#Take All Page 
all_page = soup.take_page()

#Get news in page and return to json format
news = soup.get_news(all_page)
news_json = soup.return_list_to_json(news_list=news)

#write json file
soup.write_news_to_jsonf(news_json)

# ---------------------------- Embedding and take similarity.

embedder = Embedder()

news_with_embedding = embedder.embed_news_list(news_json)
embedder.save_embedings(news_list=news_with_embedding)




