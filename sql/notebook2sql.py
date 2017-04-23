# coding=utf-8
import sqlite3
from list2sql import ListToSql

class NotebookToSql(ListToSql):
    def generate_notebook_id(self, filename, data):
        notebook_id = []
        for one_data in data:
            notebook_id.append(one_data['NotebookId'])
        with open(filename, 'wb') as f:
            f.write(str(notebook_id))

if __name__ == '__main__':
    notebooks = [{"NotebookId":"583d31a22638431de7000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":0,"Title":"Python","UrlTitle":"","NumberNotes":6,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"584950692638435007000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":1,"Title":"haKB","UrlTitle":"","NumberNotes":3,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"584f7a2126384332f1000001","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":2,"Title":"haProgress","UrlTitle":"","NumberNotes":2,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"58345e8426384358dc000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":3,"Title":"haTool","UrlTitle":"","NumberNotes":5,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"57dabf77403a8c487b000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":4,"Title":"diary","UrlTitle":"","NumberNotes":31,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"582e667f26384365aa000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":5,"Title":"GNURadio","UrlTitle":"","NumberNotes":16,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"582858ad1c1c057066000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":6,"Title":"linux","UrlTitle":"","NumberNotes":3,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"57cccf2aab644133ed0714c5","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":7,"Title":"sc-edu-work","UrlTitle":"","NumberNotes":3,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]}]

    notebook_sql = NotebookToSql()
    # notebook_sql.generate_insert_sql("notebook_insert_sql.txt", notebooks, "api_note_note") # 生成sql语句到指定文件
    # notebook_sql.generate_notebook_id("notebook_id.txt", notebooks) # 收集notebookId到数组
    sqlite_file = "D:/store/PycharmProjects/django_blog/db.sqlite3"
    sqlite_tablename = "api_note_notebook"
    # notebook_sql.insert_data_sqlite3(sqlite_file, sqlite_tablename, notebooks, False) # 将notebooks数据插入到数据库中
