import numpy as np

def cosine_similarity(vec1, vec2):
    """
    İki vektör arasındaki cosine similarity hesaplar.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def search_news(query, news_list, embedder, top_k=5):
    query_emb = embedder.embed_text(query)

    def euclidean_similarity(news_emb):
        return -np.linalg.norm(np.array(query_emb) - np.array(news_emb))

    scores = []
    for news in news_list:
        if hasattr(news, "embedding") and news.embedding:
            score = euclidean_similarity(news.embedding)
            scores.append((score, news))

    # Sort by score, not by News object
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_k]