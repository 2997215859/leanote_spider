# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import psycopg2

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

class InsertSqlPipeline(object):
    # def __init__(self, sqlite_file, sqlite_table):
    #     self.sqlite_file = sqlite_file
    #     self.sqlite_table = sqlite_table

    def __init__(self, pg_database, pg_user, pg_password, pg_host, pg_port, pg_tablename):
        self.pg_database = pg_database
        self.pg_user = pg_user
        self.pg_password = pg_password
        self.pg_host = pg_host
        self.pg_port = pg_port
        self.pg_tablename = pg_tablename
        self.item_key = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # sqlite_file = crawler.settings.get('SQLITE_FILE'), # get info from setting.py
            # sqlite_table = crawler.settings.get('SQLITE_TABLE', 'items')
            pg_database = crawler.settings.get('DATABASE'),
            pg_user = crawler.settings.get('USER'),
            pg_password = crawler.settings.get('PASSWORD'),
            pg_host = crawler.settings.get('HOST'),
            pg_port = crawler.settings.get('PORT'),
            pg_tablename = crawler.settings.get('TABLENAME')
        )

    def open_spider(self, spider):
        self.conn = psycopg2.connect(database=self.pg_database,
                                     user=self.pg_user,
                                     password=self.pg_password,
                                     host=self.pg_host,
                                     port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("SET client_encoding = UTF8;")
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):


        if len(self.item_key) == 0:
            for key in item.keys():
                self.item_key.append('"' + key + '"')



        insert_sql = "insert into {0}({1}) values({2})".format(self.pg_tablename, ','.join(self.item_key),
                                                               ','.join(['%s'] * len(item.keys())))
        # print tuple(item.values())
        try:
            self.cur.execute(insert_sql, item.values())
            self.conn.commit()
        except Exception, e:
            print "插入数据失败"
            print e
            print "noteId = ", item['NoteId']
            print "notebookId = ", item['NotebookId']
        return item

