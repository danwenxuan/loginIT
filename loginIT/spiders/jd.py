# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
	name = 'jd'
	allowed_domains = ['jd.com']
	start_urls = ['https://passport.jd.com/new/login.aspx?']

	def parse(self, response):
		yield scrapy.FormRequest.from_response(response,
											   formdata={"loginname": "qing_8125", "nloginpwd": "qing123"},
											   callback=self.parsenew)

	def parsenew(self, response):
		yield scrapy.Request(url="https://order.jd.com/center/list.action", callback=self.parsenew2)

	def parsenew2(self, response):
		with open("yinchengjd.html", "wb") as file:
			file.write(response.body)
