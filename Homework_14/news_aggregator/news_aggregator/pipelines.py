# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .db_config import session
from .models import News, Author


class NewsAggregatorPipeline:
    def process_item(self, item, spider):

        db = session()
        if not db.query(News).filter(News.title == item['title']).first():
            news = News(
                title=item['title'],
                content=item['content'],
                date=item['date'],
                img_url=item['image']
            )
            db.add(news)
            db.commit()
            db.refresh(news)
            for author in item['authors']:
                if not db.query(Author).filter(Author.name == author).first():
                    db.add(Author(name=author))
                    db.commit()
                db.query(Author).filter(Author.name == author).first().news.append(news)
                db.commit()

        db.close()
        return item

        # if not db.query(News).filter(News.title == item['title']).first():
        #     news = News(**item)
        #     db.add(news)
        #     db.commit()
        #     db.refresh(news)
        #     for author in item['author']:
        #         if not db.query(Author).filter(Author.name == author).first():
        #             db.add(Author(name=author))
        #             db.commit()
        #             db.refresh(news)
        #         author = db.query(Author).filter(Author.name == author).first()
        #         news.author.append(author)
        #         db.commit()
        #         db.refresh(news)