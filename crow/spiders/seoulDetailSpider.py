# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule

from bson.objectid import ObjectId
from crow.items import RestaurantDetailItem
from scrapy.selector import HtmlXPathSelector
from pymongo import MongoClient

class TripSpider(scrapy.Spider):
    name = "seoulDetail"
    allowed_domains = ["https://www.tripadvisor.co.kr"]
    client = MongoClient('192.168.0.21', 27017)

    db = client['trip']
    collection = db['restaurant']


    start_urls = [ "https://www.tripadvisor.co.kr%s" % s['link']
                   for s in collection.find({'_id': ObjectId("5832a0fc223dc11a5936aba3")}, { 'link': -1, '_id': 0 }) ]

    #for s in collection.find({'_id': ObjectId("5832a0fc223dc11a5936aba3")}, { 'link': -1, '_id': 0 }) ]
    #start_urls = 'https://www.tripadvisor.co.kr/Restaurant_Review-g294197-d2228988-Reviews-Myeongdong_Dakhanmari-Seoul.html'

    print start_urls

    def parse(self, response):


        hxs = HtmlXPathSelector(response)

        name = response.xpath('//title/text()').extract()[0]


        if((response.xpath('//*[@id="HEADING_GROUP"]/div/div[2]/div[2]/span/div/b/span/text()').extract() is None) == False):
            ranking = response.xpath('//*[@id="HEADING_GROUP"]/div/div[2]/div[2]/span/div/b/span/text()').extract()[0]
        else:
            ranking = '[]'

        keywords = hxs.select('//meta[@name=\'keywords\']/@content').extract()[0]
        price_range = response.xpath('//*[@class="detail first price_rating separator"]/text()').extract()
        cover_image_url = hxs.select('//meta[@property=\'og:image\']/@content').extract()[0]
        cover_image_width = hxs.select('//meta[@property=\'og:image:width\']/@content').extract()[0]
        cover_image_height = hxs.select('//meta[@property=\'og:image:height\']/@content').extract()[0]

        details = response.xpath('//*[@id="BODYCON"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]')

        content  = details.xpath('div[1]/div[2]/div[2]/text()').extract()
        content2 = details.xpath('div[1]/div[3]/div[2]/text()').extract()

        hour_range = details.xpath('div[1]/div[4]/div[2]')

        hour_range_sunday    = hour_range.xpath('div[1]/span[2]/div/text()').extract()
        hour_range_monday    = hour_range.xpath('div[2]/span[2]/div/text()').extract()
        hour_range_tuesday   = hour_range.xpath('div[3]/span[2]/div/text()').extract()
        hour_range_wednesday = hour_range.xpath('div[4]/span[2]/div/text()').extract()
        hour_range_thursday  = hour_range.xpath('div[5]/span[2]/div/text()').extract()
        hour_range_friday    = hour_range.xpath('div[6]/span[2]/div/text()').extract()
        hour_range_saturday  = hour_range.xpath('div[7]/span[2]/div/text()').extract()

        address = response.xpath('//*[@id="BODYCON"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/div/span/span/span[2]/text()').extract()
        location = response.xpath('//*[@id="taplc_neighborhood_widget_0"]/div/text()').extract()[1]
        phone_number = response.xpath('//*[@id="BODYCON"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[4]/div/span/text()').extract()

        item = RestaurantDetailItem()

        item['name'] = name
        item['ranking'] = ranking
        item['keywords'] = keywords
        item['price_range'] = price_range
        item['cover_image_url'] = cover_image_url
        item['cover_image_width'] = cover_image_width
        item['cover_image_height'] = cover_image_height
        item['content'] = content
        item['content2'] = content2

        item['hour_range_sunday'] = hour_range_sunday
        item['hour_range_monday'] = hour_range_monday
        item['hour_range_tuesday'] = hour_range_tuesday
        item['hour_range_wednesday'] = hour_range_wednesday
        item['hour_range_thursday'] = hour_range_thursday
        item['hour_range_friday'] = hour_range_friday
        item['hour_range_saturday'] = hour_range_saturday
        item['address'] = address
        item['location'] = location
        item['phone_number'] = phone_number

        yield item

        print 'name : ', name
        print 'ranking : ', ranking
        print 'keywords : ', keywords
        print 'address  : ', address
        print 'price_range  : ', price_range
        print 'location  : ', location
        print '------------------------'
        print 'cover_image_url  : ', cover_image_url
        print 'size  : ', cover_image_width, 'x', cover_image_height
        print '------------------------'
        print 'content  : ', content
        print '특이사항  : ', content2
        print '------- 운영시간 -----------------'
        print '일요일  : ', hour_range_sunday
        print '월요일  : ', hour_range_monday
        print '화요일  : ', hour_range_tuesday
        print '수요일  : ', hour_range_wednesday
        print '목요일  : ', hour_range_thursday
        print '금요일  : ', hour_range_friday
        print '토요일  : ', hour_range_saturday
        print '------- 위치 및 연락처 정보 -----------------'
        print 'address  : ', address
        print '인근지역  : ', location
        print 'phone_number  : ', phone_number
