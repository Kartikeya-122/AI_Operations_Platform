from backend.data.sample_articles import articles

def search_articles(keyword):
    results = []

    for article in articles:
        if (keyword.lower() in article["content"].lower() or keyword.lower() in article["title"].lower()):
            results.append(article)
        return results
            
