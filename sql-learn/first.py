"""
    python创建与数据库的链接
"""
import os

from pymysql import Connect

con = None
# 使用try接受可能出现的报错
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
user = (os.getenv("MYSQL_USER"))
passwd = os.getenv("MYSQL_PASSWD")
try:
    # 创建数据库链接 赋予con对象
    con = Connection = Connect(
        host=host,
        port=int(port),
        user=str(user),
        passwd=passwd,

    )
    # cursor = con.cursor()
    # err = cursor.execute("SELECT VERSION()")
    # data = cursor.fetchone()
    # logging.log(logging.INFO, f"数据库版本:{data}")
    # logging.log(logging.ERROR, f"err:{err}")
except Exception as e:
    print(f"报错:{e}")

finally:  # 无论是否报错 finally的内容会被始终执行

    if con:
        con.close()  # 关闭连接
