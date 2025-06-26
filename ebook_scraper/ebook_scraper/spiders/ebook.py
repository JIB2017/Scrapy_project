import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = [ "https://books.toscrape.com/" ]

    def parse(self, response):
        ebooks = response.css("article")

        for ebook in ebooks:
            loader = ItemLoader(item=EbookItem(), selector=ebook)

            # loader.add_value("title", ebook.css("h3 a::text").get() or ebook.css('h3 a').attrib['title'])
            # loader.add_value("price", ebook.css("p.price_color::text").get())

            loader.add_css("title", "h3 a::attr(title)")
            loader.add_css("price", "p.price_color::text")

            price_with_xpath = ebook.xpath("//p[@class = 'price_color']").get()

            # print(title, price)
            yield loader.load_item()
