from sqlalchemy import (Column, Integer, String, Text)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KnowledgeArticle(Base):
    __tablename__ = "knowledge_articles"
    
    id = Column(
        Integer,
        primary_key = True
    )
    article_id = Column(
        String,
        unique = True,
        nullable = False
    )
    title = Column(
        String,
        nullable = False
    )
    content = Column(
        Text,
        nullable = False
    )