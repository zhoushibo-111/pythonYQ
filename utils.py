import time
import pymysql
import traceback


def get_time():
    time_str = time.strftime("%Y{}%m{}%d %X")
    return time_str.format("年", "月", "日")


def get_conn():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="",
                           db="baiduchong",
                           charset="utf8")
    cursor = conn.cursor()
    return conn, cursor


def get_conn1():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="",
                           db="baiduchong",
                           charset="utf8")
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    '''
    封装通用查询
    :param sql:
    :param args:
    :return: ((),())的形式
    '''
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def update_cx():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="",
                           db="baiduchong",
                           charset="utf8")
    cursor = conn.cursor()

    sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cursor.execute(sql, [time, strftime("%Y-%m-%d"), 10, 1, 2, 3, 4, 5, 6, 7])
    conn.commit()
    cursor.close()
    conn.close()
    return req


def get_cx_data():
    # sql = "select sum(confirm)," \
    #       "(select suspect from history order by ds desc limit 1)," \
    #       "sum(heal),sum(dead) from details " \
    #       "where update_time=(select update_time from details order by update_time desc limit 1)"
    sql = "select * from total order by eid desc limit 1"
    res = query(sql)
    return res
def get_hotsearch():
    sql = "select * from hotsearch order by id desc limit 5"
    res = query(sql)
    return res

def update_details():
    conn = None
    cursor = None
    try:
        li = get_baidu_data()[1]
        conn, cursor = get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead,no_symptom) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select %s=(select update_time from details order by id desc limit 1)"  # 对比当前最大时间戳
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已经是最新数据了!")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    print(get_cx_data())
