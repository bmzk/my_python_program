'''数据库'''
from ast import Delete
import sqlite3
import time


def get_db():

    # 插入单条数据
    sql_text_2 = "INSERT INTO scores VALUES('A', '一班', '男', 96, 94, 98)"
    cur.execute(sql_text_2)

    data = [
        ('B', '一班', '女', 78, 87, 85),
        ('C', '一班', '男', 98, 84, 90),
    ]
    cur.executemany('INSERT INTO scores VALUES (?,?,?,?,?,?)', data)
    # 连接完数据库并不会自动提交，所以需要手动 commit 你的改动conn.commit()

    # 查询数学成绩大于90分的学生
    sql_text_3 = "SELECT * FROM scores WHERE 数学>90"
    cur.execute(sql_text_3)
    # 获取查询结果
    cur.fetchall()

    # 提交改动的方法
    conn.commit()


class DB():

    def __init__(self, _name: str) -> None:
        # 创建与数据库的连接
        self.conn = sqlite3.connect(_name + '.db')
        #创建一个游标 cursor
        self.cur = self.conn.cursor()
        pass

    def creat_table(self, _table, _str='ID INT PRIMARY KEY'):
        '''创建表格        语句格式：\n
        "CREATE TABLE 表名 (字段1 INT PRIMARY KEY NOT NULL, 字段2 TEXT  NOT NULL, 字段3  CHAR(50))"
        '''
        _str = 'CREATE TABLE {table} ({s})'.format(table=_table, s=_str)
        self.cur.execute(_str)
        self.conn.commit()
        print("数据表创建成功")

    def insert(self, _table, _key, _value):
        '''插入一行数据  语句格式：\n
        "INSERT INTO 表名 VALUES (值1, 值2)" \n
        "INSERT INTO 表名 (字段1, 字段2) VALUES (值1, 值2)"    '''
        _str = "INSERT INTO {table} {key} VALUES {value};".format(table=_table,
                                                                  key=_key,
                                                                  value=_value)
        self.cur.execute(_str)
        self.conn.commit()
        print("数据插入成功")

    def delete(self, _table, _key, _value):
        '''删除数据  语句格式：\n
        "DELETE FROM COMPANY WHERE ID = 7;"
        "INSERT INTO 表名 (字段1, 字段2) VALUES (值1, 值2)"    '''
        _str = "DELETE FROM {table} WHERE {key}={value};".format(table=_table,
                                                                 key=_key,
                                                                 value=_value)
        self.cur.execute(_str)
        self.conn.commit()

    def select(self, _table, _key, _condition):
        '''查询数据  语句格式：\n
        "INSERT INTO 表名 (字段1, 字段2) VALUES (值1, 值2)"    '''
        _str = "SELECT {key} FROM {table} WHERE {condition};".format(
            table=_table, key=_key, condition=_condition)
        cursor = self.cur.execute(_str)
        print('查询数据', list(cursor))
        return list(cursor)

    def update(self, _table, _k_v, _condition):
        '''查询数据  语句格式：\n
        "INSERT INTO 表名 (字段1, 字段2) VALUES (值1, 值2)"    '''
        _str = 'UPDATE {table} SET {k_v}  WHERE {condition};'.format(
            table=_table, k_v=_k_v, condition=_condition)
        self.cur.execute(_str)
        print('更新数据')

    def colse(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

def init(db:DB):
    # 创建 网线接口和 端口 对照表
    db.creat_table(_table='PORT',_str='ID INT PRIMARY KEY  NOT NULL , Line TEXT , PORT INT')


t = time.strftime('%H-%M-%S', time.localtime())
d = DB(t)
_s = 'CREATE TABLE TABLE1 (ID INT PRIMARY KEY  NOT NULL , name TEXT  NOT NULL, tt TEXT)'
d.creat_table(_s)

for i in range(9):
    d.insert('TABLE1', '(ID, name)', (i, 'a' + str(i * i + 1000)))
d.select()

d.colse()