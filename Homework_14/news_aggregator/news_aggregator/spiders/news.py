from datetime import datetime

import scrapy

next_link = 'https://forklog.com/wp-content/themes/forklogv2/ajax/getPosts.php'


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['forklog.com']
    start_urls = ['https://forklog.com/news']
    custom_settings = {'FEED_FORMAT': 'csv', 'FEED_URI': 'news.csv'}


    def parse(self, response):
        result = {}
        for post in response.css('div.post_item'):

            images = post.xpath('.//img/@src').extract()
            if len(images) > 0:
                result['image'] = images[1]
            else:
                result['image'] = None

            result['title'] = post.css('div.text_blk p::text').get()
            result['content'] = post.css('span.post_excerpt::text').get()

            result['authors'] = list(post.css('a.author_lnk::text').getall())

            date = post.css('span.post_date::text').get()
            try:
                result['date'] = datetime.strptime(date, '%d.%m.%Y').isoformat()
            except ValueError:
                print(f'Error! {date} format is not correct!')
                continue

            yield result

        # for page in range(2, 5):
        #     yield scrapy.Request(
        #         url=next_link,
        #         callback=self.parse,
        #         method='POST',
        #         body=f'page={page}',
        #         headers={'Content-Type': 'application/x-www-form-urlencoded'}
        #     )



