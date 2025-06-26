import scrapy
from ebook_scraper.items import EbookItem

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = [ "https://books.toscrape.com/" ]

    def parse(self, response):
        ebooks = response.css("article")

        for ebook in ebooks:
            ebook_item = EbookItem()

            ebook_item['title'] = ebook.css("h3 a::text").get() or ebook.css('h3 a').attrib['title']
            ebook_item['price'] = ebook.css("p.price_color::text").get()
            price_with_xpath = ebook.xpath("//p[@class = 'price_color']").get()

            # print(title, price)
            yield ebook_item
