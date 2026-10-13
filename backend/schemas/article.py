from pydantic import Basemodel

class ArticleCreate(Basemodel):
    article_id: str
    title: str
    content: str

class ArticleResponse(Basemodel):
    article_id: str
    title: str
    content: str

    class Config: 
        from_attributes = True
        