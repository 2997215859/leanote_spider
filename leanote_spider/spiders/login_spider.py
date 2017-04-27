# coding=utf-8
import scrapy
import json
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import Request, FormRequest
from leanote_spider.items import NoteItem

class LoginSpider(scrapy.Spider):
    name = 'login'
    notebook_url = "https://leanote.com/note/listNotes/?notebookId="
    note_url = "https://leanote.com/note/getNoteContent?noteId="
    notebooksId = {"583d31a22638431de7000000","584950692638435007000000","584f7a2126384332f1000001","58345e8426384358dc000000","57dabf77403a8c487b000000","582e667f26384365aa000000","582858ad1c1c057066000000","57cccf2aab644133ed0714c5"}
    headers = {"Accept":"*/*",
               "Accept-Encoding":"gzip, deflate, br",
               "Accept-Language":"zh-CN,zh;q=0.8",
               "Connection":"keep-alive",
               "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
               "Host":"leanote.com",
               "Origin":"https://leanote.com",
               "Referer":"https://leanote.com/login","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
               "X-Requested-With":"XMLHttpRequest"}
    def start_requests(self):
        # print 'Preparing login'
        return [FormRequest(url="https://leanote.com/doLogin",
                            meta={'cookiejar': 1},
                            formdata={'email':'2997215859@qq.com','pwd': '****'},                                      headers=self.headers,
                            callback=self.after_login),]

    def after_login(self, response):
        if json.loads(response.body)['Ok'] == False:
            # print  "********************* 是否 用户名 和 密码 输入错误 ? 请检查login_spider.py +26 行 ".decode('utf-8'),
            return

        for notebookId in self.notebooksId:
            # print "access url = " + self.notebook_url+notebookId
            yield Request(self.notebook_url+notebookId,
                    meta={'cookiejar': response.meta['cookiejar']},
                    headers=self.headers,
                    callback=self.get_notebook)

    def get_notebook(self, response):
        notebookdetails = json.loads(response.body_as_unicode())
        for notebookdetail in notebookdetails:
            # print "access url = " + self.note_url + notebookdetail['NoteId']
            yield Request(self.note_url + notebookdetail['NoteId'],
                          meta={'cookiejar': response.meta['cookiejar'], 'notebookdetail': notebookdetail},
                          headers=self.headers,
                          callback=self.get_note)

    def get_note(self, response):
        notedetail = json.loads(response.body_as_unicode())
        notebookdetail = response.meta['notebookdetail']
        item = NoteItem(notebookdetail)
        item['Content'] = notedetail['Content']
        item['Abstract'] = notedetail['Abstract']
        return item
