import pymysql


class Op_mysql(object):
    def __init__(self,host, user, password,db,port=3306,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset

        try:
            self.conn = pymysql.connect(host='10.10.11.38', user='fosafer', passwd='fosafer@com', db='ivr_new',port=3306, charset='utf8')
        except Exception as e:
            print('connection error %s' %e)
            quit('connection error %s' %e)
        else: #没有异常的情况下建立游标
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def execute(self,sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            print('sql error %s' %e)
            return e
        if sql[:6].upper() == 'SELECT':
            return self.cur.fetchall()
        else: #其它sql语句的话
            self.conn.commit()
            return 'OK'


    def __del__(self):
        self.cur.close()
        self.conn.close()




db1 = Op_mysql('10.10.11.38','fosafer','fosafer@com',db='ivr_new')  #实例化
print(db1.execute("delete from ivr_company where company_name = '北京文化' ;"))
print(db1.execute("delete from u_user where username = 'hello' ;"))


