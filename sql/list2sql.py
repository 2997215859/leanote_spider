# coding=utf-8
import sqlite3
import psycopg2

class ListToSql(object):
    def generate_insert_sql(self, filename, data, tablename):
        output = "Insert INTO " + tablename + "("
        for key in data[0]:
            output += '"' + key + '"' + ','
        output = output[:-1] + ")"

        for data_one in data:
            output += "select "
            for key, value in data_one.items():
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

        with open(filename, 'w') as f:
            f.write(output.encode("utf-8"))

    def insert_data_sqlite3(self, sqlite_file, sqlite_table, data, if_text_factory):
        conn = sqlite3.connect(sqlite_file) # 连接数据库
        if if_text_factory: # 处理中文字符
            conn.text_factory = str

        cur = conn.cursor() # 获取游标
        for data_one in data:
            for key, value in data_one.items():
                if isinstance(value, list):
                    data_one[key] = ','.join(data_one[key]) # 将list转化一下，否则插不进去

            insert_sql = "insert into {0}({1}) values({2})".format(sqlite_table, ','.join(data_one.keys()), ','.join(['?'] * len(data_one.keys())))
            cur.execute(insert_sql, tuple(data_one.values()))
            conn.commit()
        conn.close()


    def insert_data_postgre(self, pg_info, data, client_encoding):
        pg_database = pg_info['DATABASE']
        pg_user = pg_info['USER']
        pg_password = pg_info['PASSWORD']
        pg_host = pg_info['HOST']
        pg_port = pg_info['PORT']
        pg_tablename = pg_info['TABLENAME']
        conn = psycopg2.connect(database=pg_database, user=pg_user, password=pg_password, host=pg_host, port=pg_port)

        cur = conn.cursor()
        cur.execute("SET client_encoding = " + client_encoding + ";") # 设置客户端编码为utf8，如果输出错误乱码的话，调至gbk8，另外字段区分大小写。。所以大写务必加引号。。
        conn.commit()
        for data_one in data:
            data_one_key = []
            for key in data_one.keys():
                data_one_key.append('"' + key + '"')
            insert_sql = "insert into {0}({1}) values({2})".format(pg_tablename, ','.join(data_one_key),','.join(['%s'] * len(data_one.keys())))
            print insert_sql
            cur.execute(insert_sql, tuple(data_one.values()))

            conn.commit()
        conn.close()
