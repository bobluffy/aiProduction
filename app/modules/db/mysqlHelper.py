# -*- coding: utf-8 -*-
"""
   File Name：     mysqlHelper.py
   Description :  Mysql helper tools
   Author :       yuanfang
   date：         2019/12/20
"""
import pymysql
from dbutils.pooled_db import PooledDB
# from DBUtils.PooledDB import PooledDB


class MySQLBase(object):
    """
         依赖pymysql,logging模块
         为了提高事务处理能力,所有的事务都改为手动执行commit()
    """
    def __init__(self, host, port, user, password, db,charset='utf8'):
        '''
        初始化
        :param host:mysql服务的ip地址
        :param port:mysql服务的端口
        :param user:连接用户名
        :param password:连接密码
        :param charset:字符集默认utf-8
        :return:初始化连接
        '''
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__charset = charset
        self.db = db
        try:
            # 连接池
            print("Mysql init")
            self.__pool = PooledDB(
                creator=pymysql,  # 使用链接数据库的模块
                maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
                mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
                maxshared=1,
                blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
                setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
                ping=0,
                host=self.__host,
                port=self.__port,
                user=self.__user,
                password=self.__password,
                database=self.db,
                charset=self.__charset
            )
        except Exception as e:
            print(f"Mysql init Exception= {e} ")
            pass

    def __create_conn(self):
        conn = self.__pool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn, cursor

    def __close_conn(self, conn, cursor):
        conn.close()
        cursor.close()

    def insert(self, p_table_name, p_data):
        '''
        插入
        :param p_table_name:表名
        :param p_data: 数据需是字典类型，如：{"id": 11008,"totalCount": 298723}
        :return: 返回执行结果
        '''
        try:
            conn, cur = self.__create_conn()
            for key in p_data:
                p_data[key] = "'"+str(p_data[key])+"'"
            key = ','.join(p_data.keys())
            value = ','.join(p_data.values())
            ret_sql = "INSERT INTO " + self.db + "." + p_table_name + " (" + key + ") VALUES (" + value + ")"
            print('insert ',ret_sql)
            result = cur.execute(ret_sql)
            conn.commit()
            self.__close_conn(conn, cur)
            return True
        except pymysql.Error as e:
            print('---------mysql error=',e)
            pass

    def batch_insert(self, p_table_name, keys, values):
        '''
        插入
        :param p_table_name:表名
        :param p_data: 数据需是字典类型，如：{"id": 11008,"totalCount": 298723}
        :return: 返回执行结果
        '''

        try:
            conn, cur = self.__create_conn()
            for i, value in enumerate(values):
                for j, element in enumerate(value):
                    value[j] = "'" + element + "'"
                values[i] = '(' + ','.join(values[i]) +')'

            keys_ = ','.join(keys)
            values_ = ','.join(values)
            ret_sql = "INSERT INTO " + self.db + "." + p_table_name + " (" + keys_ + ") VALUES "+ values_
            print('---------', ret_sql)
            result = cur.execute(ret_sql)
            conn.commit()
            self.__close_conn(conn, cur)
            return True
        except pymysql.Error as e:
            print('---------mysql error=',e)
            pass

    def update(self, tableName, p_Data, where_Data):
        '''
        更新修改
        :param tableName:表名
        :param p_Data:修改的数据字典 {"hour": 23,"appid": "wwwmigu"}
        :param where_Data:where语句字典 {"id": 11004}
        :return:返回执行结果
        '''
        try:
            conn, cur = self.__create_conn()
            setData = []
            keys = p_Data.keys()
            for i in keys:
                item = "%s=%s" % (i, "'"+str(p_Data[i])+"'")
                setData.append(item)
            items = ','.join(setData)
            whereData = []
            keys = where_Data.keys()
            for i in keys:
                item = "%s=%s" % (i, "'"+str(where_Data[i])+"'")
                whereData.append(item)
            whereItems = " AND ".join(whereData)

            sql = "UPDATE " + self.db + "." + tableName +" SET "+items+" WHERE "+whereItems
            print('sql:',sql)
            result = cur.execute(sql)
            conn.commit()
            self.__close_conn(conn, cur)
            return True
        except pymysql.Error as e:
            print('---------mysql error=',e)
            return False

    def queryAll(self, sql):
        '''
        查询数据返回全部数据
        :param sql:sql语句
        :return:返回字典，如：[{'totalCount': '298723', 'id': '11002'}]
        '''
        try:
            conn, cur = self.__create_conn()
            cur.execute(sql)
            result = cur.fetchall()
            desc = cur.description
            ret_val = []
            for inv in result:
                ret_val.append(inv)
            conn.commit()
            self.__close_conn(conn, cur)
            return ret_val
        except pymysql.Error as e:
            print('---------mysql error=',e)
            pass

    def execute(self, sql):
        '''
        插入
        :param sql:需要执行的sql
        :return: 返回执行结果
        '''
        try:
            conn, cur = self.__create_conn()
            result = cur.execute(sql)
            conn.commit()
            self.__close_conn(conn, cur)
            return True
        except pymysql.Error as e:
            print('---------mysql error=', e)





