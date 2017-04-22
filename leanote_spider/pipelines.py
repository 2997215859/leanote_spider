# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class LeanoteSpiderPipeline(object):
    def __init__(self):
        self.notebook_file = open('item_notebook.jl', 'wb')
        self.note_file = open('item_note.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        if 'Abstract' in item.fields:
            self.note_file.write(line)
        else:
            self.notebook_file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()