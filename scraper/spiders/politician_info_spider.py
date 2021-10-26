import logging
import scrapy
from string import ascii_lowercase
import json

from scraper.items import Politician

class PoliticianInfoSpider(scrapy.Spider):
    """
    PoliticianSpider scrapes individual politician information from the parliament.lk website.
    """
    name = "politician_info"
    politicians = []

    def start_requests(self):
        """
        Sends a HTTP request for each of the politician. (225)
        """
        url = "https://www.parliament.lk/en/members-of-parliament/directory-of-members/viewMember/{mem_intranet_id}"
        politicians = self.get_politicians()
        for politician in politicians:
            yield scrapy.Request(url=url.format(mem_intranet_id=politician["mem_intranet_id"]), callback=self.parse)

    def parse(self, response):
        """
        Parses the politician info html page, extracts the required information if available
        and save as a JSON file.
        """
        self.log(response, logging.DEBUG)
        name = response.xpath('//div[@class="components-wrapper"]/h2/text()').get()
        party = response.xpath('//div[@class="bottomdiv1"]/table/tr/td/a/text()').get()
        # Portofolio not present in every politician page.
        temp = response.xpath('//div[@class="bottomdiv1"]/table/tr/td/div/text()').extract()[1]
        portfolio = ""
        if temp == "Portfolio":
            portfolio = response.xpath('//div[@class="bottomdiv1"]/table/tr/td/text()').extract()[1].split("\r\n")[1].strip()
            electoral = response.xpath('//div[@class="bottomdiv1"]/table/tr/td/text()').extract()[2].split("\r\n")[1].strip()
        else:
            electoral = response.xpath('//div[@class="bottomdiv1"]/table/tr/td/text()').extract()[1].split("\r\n")[1].strip()
        self.log("data:{},{},{}, {}".format(name ,party, electoral, portfolio))

        # Extracts dob, civil_status, religion, occupation, career.
        left_wrap_keys = response.xpath('//div[@class="left-wrap"]/div/table/tr/td/span/text()').extract()
        left_wrap_values = response.xpath('//div[@class="left-wrap"]/div/table/tr/td/text()').extract()
        assert len(left_wrap_keys) == len(left_wrap_values), "left wrap keys and values mismatch"
        dob, civil_status, religion, occupation, career = "","","","", ""
        for i, key in enumerate(left_wrap_keys):
            if key == "Date of Birth":
                dob = left_wrap_values[i].split(":")[1].strip()
            if key == "Civil Status":
                civil_status = left_wrap_values[i].split(":")[1].strip()
            if key == "Religion":
                religion = left_wrap_values[i].split(":")[1].strip()
            if key == "Profession / Occupation":
                occupation = left_wrap_values[i].split(":")[1].strip()
        # Career is optional most of the time.
        career = response.xpath('//div[@class="top-mp-detail-3"]/div/pre/text()').get()
        committees = response.xpath('//div[@class="top-mp-detail-4"]/div/div/ul/li/a/text()').extract()
        politician = Politician(name=name, party=party, portfolio= portfolio, 
        electoral = electoral, dob = dob, civil_status = civil_status, religion = religion, occupation = occupation, career=career, committees=committees)
        output = open("corpus/en/{mem_intranet_id}.json".format(mem_intranet_id = response.url.split("/")[-1]), "w+")
        output.write(politician.toJSON())
        print(politician)

    def get_politicians(self):
        politician_list = open("politicians.json", "r")
        arr = json.load(politician_list)
        return arr


