# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import TakeFirst, MapCompose

def get_price(price):
    return float(price.replace("£",""))

class EbookItem(Item):
    title = Field(
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()
    )
