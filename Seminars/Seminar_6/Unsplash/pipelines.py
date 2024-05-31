# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline

import csv

class CsvWriterPipeline:
    def __init__(self):
        self.file = open('items.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=['url', 'name', 'categories', 'photo'])
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()


class UnsplashPipeline:
    def process_item(self, item, spider):
        print()
        return item

class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photo']:
            #for img_url in item['photo']:
            try:
                yield scrapy.Request(item['photo'])
            except Exception as e:
                print(e)