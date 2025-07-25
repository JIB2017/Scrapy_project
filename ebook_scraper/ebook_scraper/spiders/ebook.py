import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = [ 
        "https://books.toscrape.com/", 
        "https://books.toscrape.com/catalogue/category/books/mystery_3", 
        "https://books.toscrape.com/catalogue/category/books/sequential-art_5"
        ]
    cols = ["Title", "Price"]

    # def __init__(self):
    #     super().__init__()
    #     self.page_count = 1
    #     self.page_total = 4

    # async def start(self):
    #     base_url = self.start_urls[2]
    #     # Pagination
    #     while self.page_count <= self.page_total:
    #         yield scrapy.Request(
    #             f"{base_url}/page-{self.page_count}.html"
    #         )
    #         self.page_count += 1
        # return super().start()

    def parse(self, response):
        ebooks = response.css("article")

        for ebook in ebooks:
            loader = ItemLoader(item=EbookItem(), selector=ebook)
            url_base = "https://books.toscrape.com/catalogue/"
            url = ebook.css("h3 a::attr(href)").re(r'^(\.\./)+(.+)')[1]

            # loader.add_value("title", ebook.css("h3 a::text").get() or ebook.css('h3 a').attrib['title'])
            # loader.add_value("price", ebook.css("p.price_color::text").get())

            # loader.add_css("title", "h3 a::attr(title)")
            # loader.add_css("price", "p.price_color::text")

            # price_with_xpath = ebook.xpath("//p[@class = 'price_color']").get()

            # print(title, price)
            # yield loader.load_item()
            yield scrapy.Request(
                url = url_base + url,
                callback = self.parse_details
            )
        
        # has_next_page = response.css("li.next a")

        # if (has_next_page):
        #     next_url = f"{self.start_urls[1]}/{has_next_page.attrib['href']}"
        #     yield scrapy.Request(next_url)
    def parse_details(self, response):
        main = response.css("div.product_main")
        loader = ItemLoader(item=EbookItem(), selector=main)

        loader.add_css("title", "h1::text")
        loader.add_css("price","p.price_color::text")
        
        quantity = main.css("p.availability")
        loader.add_value("quantity", quantity.re(r'\(.+ available\)')[0])

        yield loader.load_item()
