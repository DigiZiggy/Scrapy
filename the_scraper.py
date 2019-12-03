# encoding: utf-8
"""
Program to crawl over https://ordi.eu website and scrape the site
for all the computers names, prices and product photos.

:author: Sigrid Närep
"""
import scrapy


class GetComputersSpider(scrapy.Spider):
    name = "get_computers_spider"
    start_urls = ['https://ordi.eu/lauaarvutid?___store=en&___from_store=et']

    def parse(self, response):
        """
        Using CSS selectors since it is the easiest way of finding information about all the
        items on the page. Passing selector .item to response object because each computer
        is within that CSS class in page html.

        :param response:
        :return:
        """
        SET_SELECTOR = '.item'
        for computer in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h2 a::text'
            PRICE_SELECTOR = '.price-box span::text'
            IMAGE_SELECTOR = '.product-image img::attr(src)'
            yield {
                'Product name': computer.css(NAME_SELECTOR).get(),
                'Price': computer.css(PRICE_SELECTOR).get(),
                'Picture href': computer.css(IMAGE_SELECTOR).get(),
            }

            NEXT_PAGE_SELECTOR = '.next::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).get()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
