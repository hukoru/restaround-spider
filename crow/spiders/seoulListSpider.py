# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule

from crow.items import RestaurantItem
from scrapy.selector import HtmlXPathSelector

class TripSpider(scrapy.Spider):
    name = "trip"
    allowed_domains = ["https://www.tripadvisor.co.kr/Restaurants-g294197-Seoul.html"]

    #3994*30 페이지 까지 있
    start_urls = ['https://www.tripadvisor.co.kr/RestaurantSearch?Action=PAGE&geo=294197&ajax=1&itags=10591&sortOrder=popularity&o=a%d' %(n*30) for n in range(0, 3995)]


    def parse(self, response):

        hxs = HtmlXPathSelector(response)

        shortSellDetails = hxs.select("//div[@class='shortSellDetails']/h3")

        restaurant = 1
        titles = response.xpath('//*[@class="shortSellDetails"]/h3/a/text()').extract()
        links = response.xpath('//*[@class="shortSellDetails"]/h3/a[1]/@href').extract()

        for shortSellDetail in shortSellDetails:

            item = RestaurantItem()

            title = shortSellDetail.select("a/text()").extract()[0]
            link = shortSellDetail.select("a[1]/@href").extract()[0]

            item['title'] = title
            item['link'] = link
            item['restaurant_id'] = restaurant
            restaurant += 1

            yield item


        #for title in titles:
            #print title
