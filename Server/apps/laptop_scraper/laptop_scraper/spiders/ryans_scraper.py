# -*- coding: utf-8 -*-
import scrapy
from scrapy_djangoitem import DjangoItem

import django
django.setup()
from apps.database_manager.models import laptop_properties

class RyansScraperSpider(scrapy.Spider):
    name = 'ryans_scraper'
    allowed_domains = ['ryanscomputers.com']
    start_urls = ['http://ryanscomputers.com/grid/notebook--component-notebook?page=1&limit=72',
    'http://ryanscomputers.com/grid/notebook--component-notebook?page=2&limit=72',
    'http://ryanscomputers.com/grid/notebook--component-notebook?page=3&limit=72',
    'http://ryanscomputers.com/grid/notebook--component-notebook?page=4&limit=72',
    'http://ryanscomputers.com/grid/notebook--component-notebook?page=5&limit=72',
    'http://ryanscomputers.com/grid/notebook--component-notebook?page=6&limit=72',
    'http://ryanscomputers.com/grid/notebook--component-notebook?page=7&limit=72'
    ]

    count = 0
    
    def parse(self, response):
        # title = response.css('title::text').extract()
        # yield {'title_text' : title}
        laptop_links = response.css("#produt-container .row .col-sm-4.col-md-4.col-lg-4 .product-box .product-thumb a::attr(href)").getall()

        
        for link in laptop_links:
            yield scrapy.Request(link, callback=self.parse_laptop_page)
        
        

    def parse_laptop_page(self, response):

        laptop_data = {}

        laptop_data['image_url'] = response.xpath('//img[@id="listMainImg"]').attrib['src']
        
        table = response.css('td::text').getall()

        for _ in range(int(len(table)/2)):
            key = table.pop(0)
            value = table.pop(0)
            laptop_data[key] = value

        laptop_data['price'] = int(response.css('.price::text').get().split()[1].replace(',', ''))

        laptop = laptop_item()
        laptop['lapID'] = str(self.count)
        laptop['lapBrand'] = laptop_data['Model'].split()[0]
        laptop['lapModel'] = ' '.join(laptop_data['Model'].split()[1:])
        ram_type = ''
        try:
            ram_type = laptop_data['Ram Type']
        except:
            pass
        laptop['ram'] = " ".join([laptop_data['Ram'], ram_type])
        laptop['processor'] = laptop_data['Processor Model']
        laptop['gpu'] = laptop_data['Graphics Chipset']
        laptop['purpose'] = 'N/A'
        laptop['price'] = laptop_data['price']
        laptop['url'] = response.url
        laptop['image_url'] = laptop_data['image_url']
        laptop['rating'] = 0    # ryans does not have enough customer ratings

        laptop.save()
        
        self.count = self.count + 1

        yield {'laptop' : laptop['lapModel']}


class laptop_item(DjangoItem):
    django_model = laptop_properties