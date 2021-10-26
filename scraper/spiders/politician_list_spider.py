import scrapy
from string import ascii_lowercase
import json

class PoliticianListSpider(scrapy.Spider):
    """
    PoliticianSpider scrapes the list of politicians from the parliament.lk website.
    """
    name = "politician_list"
    politicians = []

    def start_requests(self):
        """
        Sends a HTTP request for each of the alphabetic letter.
        """
        url = "https://www.parliament.lk/members-of-parliament/index2.php?option=com_members&task=all&tmpl=component&letter={letter}"
        for letter in ascii_lowercase:
            yield scrapy.Request(url=url.format(letter=letter), callback=self.parse)

    def parse(self, response):
        """
        Concatenates the JSON lists for each of the HTTP requests and write the output to a file as a JSON array.
        """
        self.politicians.extend(response.json())
        self.log(len(self.politicians))
        if len(self.politicians) == 225:
            file = open("politicians.json", "w")
            json.dump(self.politicians, file)
