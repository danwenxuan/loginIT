# -*- coding: utf-8 -*-
import scrapy


class CtonimeiSpider(scrapy.Spider):
    name = 'ctonimei'
    allowed_domains = ['51cto.com']
    start_urls = ['http://home.51cto.com/index']

    def parse(self, response):
        yield  scrapy.FormRequest.from_response(response,
                                                formdata={"LoginForm[username]": "batmanken@126.com",
                                                          "LoginForm[password]": "abcd1234"},
                                                callback = self.parsenew)

    def parsenew(self,response):
        yield scrapy.Request(url="http://home.51cto.com/space?uid=1945833", callback=self.parsenew2)# 登录喉的界面

    def parsenew2(self,response):
        with open("51cto.html","wb") as file:
            file.write(response.body)
