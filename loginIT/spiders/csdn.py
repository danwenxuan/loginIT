# -*- coding: utf-8 -*-
import scrapy


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://passport.csdn.net/account/login?']

    def parse(self, response):
        yield  scrapy.FormRequest.from_response(response,
                                                formdata={"username": "yincheng0571", "password": "yinchengak47.net"},
                                                callback = self.parsenew)

    def parsenew(self,response):
        yield scrapy.Request(url="http://my.csdn.net/my/mycsdn",callback=self.parsenew2)

    def parsenew2(self,response):
        with open("wenxuancsdn.html","wb") as file:
            file.write(response.body)
