from database.connection import(SessionLocal)
from sqlalchemy.orm import Session
from backend.database.models import(KnowledgeArticle)

class ArticleRepository:
    def get_all(self, db: Session):
        return db.query(KnowledgeArticle).all()

    def get_by_article_id(self, db: Session, article_id: str):
        return(db.query(KnowledgeArticle).filter(KnowledgeArticle.article_id == article_id).first())

    def create(self, db: Session, article):
        db.add(article)
        db.commit()
        db.refresh(article)
        return article
    
    def search(self, db: Session, keyword: str):
        pattern = f"%{keyword}%"
        return(db.query(KnowledgeArticle).filter(KnowledgeArticle.title.ilike(pattern)|KnowledgeArticle.content.ilike(pattern)).all())
