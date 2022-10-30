from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from datetime import datetime
from .db_config import Base


many_to_many = Table(
    'news_authors',
    Base.metadata,
    Column('news_id', Integer, ForeignKey('news.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    img_url = Column(String(250), nullable=True)
    author = relationship('Author', secondary=many_to_many, back_populates='news')


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    news = relationship('News', secondary=many_to_many, back_populates='author')


