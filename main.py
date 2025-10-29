from models.models import Soup
import warnings
warnings.filterwarnings("ignore")

# Create a Soup() object
soup = Soup()

#Take All Page 
all_page = soup.take_page()

#Get news in page and return to json format
news = soup.get_news(all_page)
news_json = soup.return_list_to_json(news_list=news)

#write json file
soup.write_news_to_jsonf(news_json)






