# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import TakeFirst, MapCompose

def get_price(price):
    return float(price.replace("£",""))

def get_quantity(quantity):
    return quantity.replace('(','').split()[0]

class EbookItem(Item):
    title = Field(
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()
    )
    quantity = Field(
        input_processor=MapCompose(get_quantity),
        output_processor=TakeFirst()
    )
