# 📰 News Embedding and Similarity Search

This project implements a powerful news article similarity search system using embeddings and semantic similarity. It scrapes news articles from Hürriyet's RSS feed, generates embeddings using a local embedding model, and allows users to search for similar news articles using natural language queries.

## 🌟 Features

- **Web Scraping**: Automatically scrapes news articles from Hürriyet's RSS feed
- **Embedding Generation**: Uses the `nomic-embed-text` model for generating text embeddings
- **Similarity Search**: Implements both cosine and Euclidean similarity metrics
- **Caching**: Saves scraped news and embeddings to avoid redundant processing
- **Interactive Search**: User-friendly command-line interface for news search

## 🛠️ Technical Architecture

The project is organized into several key components:

- `models/`
  - `models.py`: Core classes (`News`, `Soup`, `Embedder`)
  - `similarity.py`: Similarity calculation functions
  - `__init__.py`: Package initialization
- `data/`
  - `news.json`: Cached scraped news articles
  - `embedded.json`: Cached news embeddings
- `main.py`: Entry point and orchestration

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/ofowardar/embedding-news-with-bs4.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## 💡 Usage

1. The program will first scrape news articles if they haven't been cached
2. It will then generate embeddings for the articles (if not already cached)
3. You'll be prompted to enter a search query
4. The system will return the top 4 most similar news articles with their similarity scores

## 🔧 Configuration

The system uses several configurable parameters:

- `NEWS_URL`: RSS feed URL (default: Hürriyet Gündem)
- `model_name`: Embedding model (default: "nomic-embed-text:latest")
- `base_url`: Local embedding service URL
- `top_k`: Number of similar articles to return (default: 4)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

---

Created by [ofowardar](https://github.com/ofowardar)
Contact With Me on LinkedIN [Omer Faruk Ozvardar](https://www.linkedin.com/in/ofowardar)