import sqlalchemy from create_engine 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ("postgresql://postgres:"Pianoguitar122()""@localhost:5432/ai_operations_platfrom"")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)