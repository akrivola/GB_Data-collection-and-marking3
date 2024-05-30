import scrapy
from scrapy.http import HtmlResponse
from items import UnsplashItem

class UnsplSpider(scrapy.Spider):
    name = "Unspl"
    allowed_domains = ["unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@class='Prxeh']")
        for link in links:
            yield response.follow(link, callback=self.parse_photo)

    def parse_photo(self, response: HtmlResponse):
        name = response.xpath('//title/text()').get()
        categories = response.xpath("//a[@class='VyS40 GcCli p4rnw']/text()").getall()
        url = response.url
        photo = response.xpath("//div[@class='WxXog']/img/@src").get()
        yield(UnsplashItem(name=name, categories=categories, url=url, photo=photo))
