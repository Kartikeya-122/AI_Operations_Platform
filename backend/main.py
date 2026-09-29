# from services.search_service import search_articles

# keyword = input("Enter keyword: ")
# results = search_articles(keyword)
# print()

# if not results:
#     print("No matching records found.")
# else:
#     for article in results:
#         print("=" * 50)
#         print(article["title"])
#         print(article["content"])




from backend.data.sample_articles import articles
from fastapi import FastAPI
from fastapi import HTTPException
app = FastAPI()

@app.get("/")
def root():
    return{
        "message": "Enterprise AI Operations Platform"
    }

@app.get("/health")
def health():
    return{
        "Status": "healthy"
    }

@app.get("/articles")
def get_articles():
    return articles

@app.get("/articles/{article_id}")
def get_article(article_id:str):
    for article in articles:
        if article["id"] == article_id:
            return article
        
    raise HTTPException(status_code=404, detail="Article not found")

from backend.schemas.search_request import(SearchRequest)
from backend.services.search_service import(search_articles)

@app.post("/Search")
def search(request:SearchRequest):
    results = search_articles(request.keyword)
    return{"results": results}




