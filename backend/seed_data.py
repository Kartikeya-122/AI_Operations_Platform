from database.connection import(SessionLocal)
from database.models import(KnowledgeArticle)

db = SessionLocal()
articles = [
    KnowledgeArticle(
        article_id = "KB001",
        title = "MID Server Failure",
        content = """
        Check firewall.
        Check Certicficates.
        Check ECC Queue.
        """
    ),
    KnowledgeArticle(
        article_id = "KB002",
        title = "Discovery Timeout",
        content = """
        Verify Credentials.
        Verify Connectivity.
        """
    )
]   
db.add_all(articles)
db.commit()
print("Data inserted")