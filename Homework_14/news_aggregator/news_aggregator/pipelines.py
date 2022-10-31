# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from .db_config import engine
from .models import News, Author, Base


class NewsAggregatorPipeline:

    def __init__(self):
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        self.session = session()

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        with self.session as db:

            # Check if the news is already in the database
            if not db.query(News).filter_by(title=adapter['title']).first():

                news = News(
                    img_url=adapter['image'],
                    title=adapter['title'],
                    content=adapter['content'],
                    date=adapter['date'],
                )

                # Check if the author is already in the database
                for author_name in adapter['authors']:
                    author_name = author_name.strip()
                    author = db.query(Author).filter_by(name=author_name).first()

                    if not author:
                        new_author = Author(name=author_name)
                        news.author.append(new_author)
                        db.add(new_author)
                        db.commit()
                        print('Author added to the database')
                    else:
                        news.author.append(author)
                        print('Author already exists')

                db.add(news)
                db.commit()
                print('News added to the database')

        print('NewsItem added to the database')
        return item
