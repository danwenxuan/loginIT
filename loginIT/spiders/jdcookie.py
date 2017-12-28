#!usr/bin/python/
# -*-conding:utf-8-*-
# -*- coding: utf-8 -*-
import scrapy


class JDcnimeiSpider(scrapy.Spider):
	name = 'jdcookie'
	allowed_domains = ['jd.com']
	start_urls = ['https://order.jd.com/center/list.action']
	cookie = {
		"_jdv": "122270672|direct|-|none|-|1514454847151",
		"PCSYCityID": "1607, _jrda:1",
		"UM_distinctid": "1609c8fd765101-0923d6b233b031-2b6f686a-100200-1609c8fd768308",
		"CNZZDATA1256793290": "2080565007-1514450405-https%253A%252F%252Fwww.jd.com%252F%7C1514450405",
		"wlfstk_smdl": "krxgfczs8tbytk9t0v3qhhaqbvfszq0j",
		"_jrdb": "1514456430018",
		"TrackID": "1YwDNAOClL1YrGFqek_3u2x4vvBG_HoHK1bA6Rpyfqr6ann-P32Fyk8T6uyMixeHUtILeOwYu0DCgTX2xJ_H3oFgy5HlCX30XHgirPUe18lI",
		"pinId": "8GhAS_l4jAT-OfVgDyQg2Q",
		"pin": "WENZIXUAN332",
		"unick": 'WENZIXUAN332',
		"thor": "9A3857F44B8A19B8B0072C23AC173843EDA6135DE8740DBB6D5C4FFB71655555A34EDBB6A3288AF0E83181FA7030AC2A7C0D79CE95250FAF8E6EB6DB27B070C9B4643FDF3FAA65BD05EE65AFCDA2AFB4A0D165CC92B96B35F3036B9DC90027D3CB2987D3C122EFB6B407A4FFAE83404246FFD3B18AC34810F2D5984108909BC8F7DBD6149B4A7662B5EF8C3AD9C65DD9",
		"_tp": "fjvowk4Isr9PFDsbaen%2BhQ%3D%3D",
		"_pst": "WENZIXUAN332",
		"ceshi3.com": "103",
		"__jda": "122270672.1984859939.1508328323.1512872210.1514454847.7",
		"__jdb": "122270672.10.1984859939|7.1514454847",
		"__jdc": "122270672",
		"3AB9D23F7A4B3C9B": "5MY2RZEUHGVUZWNGQPJHAE3WS5QG3EVLT3346MECAZWULGZD34OEON7T7OGN3OWKBVVAXCDVNRXERJQ3CUKL5QNQMI",
		"__jdu": "1984859939"
	}

	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.FormRequest(url, cookies=self.cookie, callback=self.parse_page)

	def parse_page(self, response):
		with open("jdcookie.html", "wb") as file:
			file.write(response.body)
