import scrapy
from scrapy.selector import Selector
from WeatherData.items import WebItem

class TianqiSpider(scrapy.spiders.Spider):
    name = "Tianqi"
    allowed_domains = ["timeanddate.com/"]
    start_urls = [
        "https://www.timeanddate.com/weather/@1912606/hourly",
    ]

    def parse(self, response):

        sel = Selector(response)
        title = sel.xpath('//title').extract()
        sites = sel.xpath('//tbody/tr')

        for site in sites:
            item = WebItem()
            item['time'] = site.xpath('th/text()').extract()
            item['temp'] = site.xpath('td/text()')[0].extract().replace(u'\xa0', u' ')
            item['Weather'] = site.xpath('td/text()')[1].extract().replace(u'\xa0', u' ')
            item['Feels_Like'] = site.xpath('td/text()')[2].extract().replace(u'\xa0', u' ')
            item['Wind'] = site.xpath('td/text()')[3].extract().replace(u'\xa0', u' ')
            item['Humidity'] = site.xpath('td/text()')[4].extract().replace(u'\xa0', u' ')
            item['Chance'] = site.xpath('td/text()')[5].extract().replace(u'\xa0', u' ')
            item['Amount'] = site.xpath('td/text()')[6].extract().replace(u'\xa0', u' ')

            #filename = title
            #open(filename, 'wb').write("1111")
            print(item['time'])
            print(item['temp'])
            print(item['Wind'])
            print(item['Humidity'])
