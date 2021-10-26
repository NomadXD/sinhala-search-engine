# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json

class Politician(scrapy.Item):
    name = scrapy.Field()
    party = scrapy.Field()
    portfolio = scrapy.Field()
    electoral = scrapy.Field()
    dob = scrapy.Field()
    civil_status = scrapy.Field()
    religion = scrapy.Field()
    occupation = scrapy.Field()
    career = scrapy.Field()
    committees = scrapy.Field()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

