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

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return{
        "message": "Enterprise AI Operations Platform"
    }