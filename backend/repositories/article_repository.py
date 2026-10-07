from database.connection import(SessionLocal)
from database.models import(KnowledgeArticle)

class ArticleRepository:
    def get_all(self):
        db = SessionLocal()
        return db.query(KnowledgeArticle).all()