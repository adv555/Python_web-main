from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///sql_news.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)




