# coding=utf-8
notebooks = [{"NotebookId":"583d31a22638431de7000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":0,"Title":"Python","UrlTitle":"","NumberNotes":6,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"584950692638435007000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":1,"Title":"haKB","UrlTitle":"","NumberNotes":3,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"584f7a2126384332f1000001","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":2,"Title":"haProgress","UrlTitle":"","NumberNotes":2,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"58345e8426384358dc000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":3,"Title":"haTool","UrlTitle":"","NumberNotes":5,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"57dabf77403a8c487b000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":4,"Title":"diary","UrlTitle":"","NumberNotes":31,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"582e667f26384365aa000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":5,"Title":"GNURadio","UrlTitle":"","NumberNotes":16,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"582858ad1c1c057066000000","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":6,"Title":"linux","UrlTitle":"","NumberNotes":3,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]},{"NotebookId":"57cccf2aab644133ed0714c5","UserId":"57cccf2aab644133ed0714c2","ParentNotebookId":"","Seq":7,"Title":"sc-edu-work","UrlTitle":"","NumberNotes":3,"IsTrash":False,"IsBlog":False,"CreatedTime":"0001-01-01T00:00:00Z","UpdatedTime":"0001-01-01T00:00:00Z","IsWX":False,"Usn":0,"IsDeleted":False,"Subs":[]}];

notebook_id = []
table_name = "api_note_notebook"
output = "Insert INTO " + table_name + "("
for key in notebooks[0]:
    output += key + ","
output = output[:-1] + ")"
for notebook in notebooks:
    notebook_id.append(notebook['NotebookId'])
    output += "select "
    for key, value in notebook.items():
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
with open('notebook_insert_sql.txt', 'w') as f:
    f.write(output.encode("utf-8"))

with open('notebook_id.txt', 'w') as f:
    f.write(str(notebook_id))