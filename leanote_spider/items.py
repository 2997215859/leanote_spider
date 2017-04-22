# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class NotebookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    NoteId = Field()
    UserId = Field()
    CreatedUserId = Field()
    NotebookId = Field()
    Title = Field()
    Desc = Field()
    Src = Field()
    ImgSrc = Field()
    Tags = Field()
    IsTrash = Field()
    IsBlog = Field()
    UrlTitle = Field()
    IsRecommend = Field()
    IsTop = Field()
    HasSelfDefined = Field()
    ReadNum = Field()
    LikeNum = Field()
    CommentNum = Field()
    IsMarkdown = Field()
    AttachNum = Field()
    CreatedTime = Field()
    UpdatedTime = Field()
    RecommendTime = Field()
    PublicTime = Field()
    UpdatedUserId = Field()
    Usn = Field()
    IsDeleted = Field()
    IsPublicShare = Field()

class NoteItem(Item):
    Abstract = Field()
    Content = Field()
    CreatedTime = Field()
    IsBlog = Field()
    NoteId = Field()
    UpdatedTime = Field()
    UpdatedUserId = Field()
    UserId = Field()
