# coding:utf-8
tagsJson = [{"TagId":"584920d3ab6441703200ec9c","UserId":"57cccf2aab644133ed0714c2","Tag":"GNU Radio","Usn":4656,"Count":13,"CreatedTime":"2016-12-08T16:58:59.984+08:00","UpdatedTime":"2017-04-14T15:38:09.348+08:00","IsDeleted":False},{"TagId":"58eb495cab6441740600fb16","UserId":"57cccf2aab644133ed0714c2","Tag":"django","Usn":11571,"Count":3,"CreatedTime":"2017-04-10T16:59:08.713+08:00","UpdatedTime":"2017-04-13T15:29:39.888+08:00","IsDeleted":False},{"TagId":"5849300fab6441703200ee48","UserId":"57cccf2aab644133ed0714c2","Tag":"python","Usn":4800,"Count":5,"CreatedTime":"2016-12-08T18:03:59.707+08:00","UpdatedTime":"2017-04-13T15:29:36.365+08:00","IsDeleted":False},{"TagId":"58492fffab6441703200ee47","UserId":"57cccf2aab644133ed0714c2","Tag":"linux","Usn":4796,"Count":2,"CreatedTime":"2016-12-08T18:03:43.146+08:00","UpdatedTime":"2017-04-07T16:38:36.297+08:00","IsDeleted":False},{"TagId":"58492f36ab6441378102a166","UserId":"57cccf2aab644133ed0714c2","Tag":"周报","Usn":4773,"Count":15,"CreatedTime":"2016-12-08T18:00:22.413+08:00","UpdatedTime":"2017-03-29T00:44:10.54+08:00","IsDeleted":False},{"TagId":"5857421aab64416d7600f7ff","UserId":"57cccf2aab644133ed0714c2","Tag":"password","Usn":7017,"Count":1,"CreatedTime":"2016-12-19T10:12:42.145+08:00","UpdatedTime":"2016-12-19T10:12:42.145+08:00","IsDeleted":False},{"TagId":"58493023ab6441378102a173","UserId":"57cccf2aab644133ed0714c2","Tag":"爬虫","Usn":4803,"Count":1,"CreatedTime":"2016-12-08T18:04:19.36+08:00","UpdatedTime":"2016-12-08T18:04:19.36+08:00","IsDeleted":False},{"TagId":"5849300cab6441378102a172","UserId":"57cccf2aab644133ed0714c2","Tag":"sublime","Usn":4798,"Count":1,"CreatedTime":"2016-12-08T18:03:56.867+08:00","UpdatedTime":"2016-12-08T18:03:56.867+08:00","IsDeleted":False},{"TagId":"58492ef1ab6441703200ee36","UserId":"57cccf2aab644133ed0714c2","Tag":"每日学习","Usn":4764,"Count":7,"CreatedTime":"2016-12-08T17:59:13.992+08:00","UpdatedTime":"2016-12-08T18:00:06.442+08:00","IsDeleted":False},{"TagId":"58492e5aab6441378102a148","UserId":"57cccf2aab644133ed0714c2","Tag":"GRC","Usn":4754,"Count":1,"CreatedTime":"2016-12-08T17:56:42.931+08:00","UpdatedTime":"2016-12-08T17:56:42.931+08:00","IsDeleted":False},{"TagId":"58492175ab64413781029fca","UserId":"57cccf2aab644133ed0714c2","Tag":"红色","Usn":4694,"Count":0,"CreatedTime":"2016-12-08T17:01:41.709+08:00","UpdatedTime":"2016-12-08T17:51:04.758+08:00","IsDeleted":False},{"TagId":"583505fbab6441378100f0fa","UserId":"57cccf2aab644133ed0714c2","Tag":"黄色","Usn":2217,"Count":0,"CreatedTime":"2016-11-23T10:59:07.223+08:00","UpdatedTime":"2016-12-08T17:03:04.454+08:00","IsDeleted":False},{"TagId":"584920f7ab6441703200eca2","UserId":"57cccf2aab644133ed0714c2","Tag":"蓝色","Usn":4666,"Count":0,"CreatedTime":"2016-12-08T16:59:35.753+08:00","UpdatedTime":"2016-12-08T16:59:37.326+08:00","IsDeleted":False}];

table_name = "api_note_tag"
output = "Insert INTO " + table_name + "("
for key in tagsJson[0]:
    output += key + ","
output = output[:-1] + ")"
for tagJson in tagsJson:
    output += "select "
    for key, value in tagJson.items():
        if isinstance(value, int):
            if str(value) == "True":
                output += "'true',"
            elif str(value) == "False":
                output += "'false',"
            else:
                output += str(value) + ","
        elif isinstance(value, list):
            output += '"' + ",".join(value).decode("utf-8") + '"' + ","
        else:
            output += '"' + value.decode("utf-8") + '"' + ','
    output = output[:-1] + " union all "
output = output[:-10]
with open('tag_insert_sql.txt', 'w') as f:
    f.write(output.encode("utf-8"))

