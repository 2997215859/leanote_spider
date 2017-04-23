# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sqlite3

class GetCommonJsonFilePipeline(object):
    def __init__(self):
        self.notebook_file = codecs.open('item_notebook.jl', 'wb', encoding='utf-8')
        self.note_file = codecs.open('item_note.jl', 'wb', encoding='utf-8')
        self.note_file = codecs.open('item_sql_note', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        self.get_common_json_file(item)
        return item;

    def close_spider(self, spider):
        self.file.close()

    def get_common_json_file(self, item):
        # just write json to file
        line = json.dumps(dict(item)) + '\n'
        if 'Content' in item.fields:
            self.note_file.write(line.decode('unicode_escape'))
        else:
            self.notebook_file.write(line.decode('unicode_escape'))

class InsertSqlitePipeline(object):
    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file = crawler.settings.get('SQLITE_FILE'), # get info from setting.py
            sqlite_table = crawler.settings.get('SQLITE_TABLE', 'items')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        item['Tags'] = ",".join(item['Tags'])
        insert_sql = "insert into {0}({1}) values({2})".format(self.sqlite_table, ','.join(item.keys()), ','.join(['?'] * len(item.keys())))
        self.cur.execute(insert_sql, item.values())
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()