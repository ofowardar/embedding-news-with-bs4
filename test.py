from models.models import Soup
from models.models import Embedder
import warnings

warnings.filterwarnings('ignore')

# Haberleri çek
soup_obj = Soup()
all_page = soup_obj.take_page()
news_list = soup_obj.get_news(all_page)  # <-- News objeleri listesi

# Embedding al
embedder = Embedder()
news_with_embedding = embedder.embed_news_list(news_list)  # <-- artık doğru

# Kaydet
embedder.save_embedings(news_list=news_with_embedding,path="C:/Users/Ömer Faruk Özvardar/Desktop/Makine Öğrenimi Ödev/data/embedded.json")
