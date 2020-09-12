from urllib import request
import re
import time
import pymysql
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='baiduchong')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 无头  option = ChromeOptions()
# option.add_argument("--headless")
def get_baidu_hot():
    browser = webdriver.Chrome(r'C:\chrome\chromedriver.exe')
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab1"
    wait = WebDriverWait(browser, 10)
    browser.get(url)
    time.sleep(1)

    but = browser.find_elements_by_xpath('//*[@id="ptab-1"]/div[3]/div/div[2]/a/div')

    content = [i.text for i in but]
    return content


def update_hot():

        content = get_baidu_hot()
        print(f"{time.asctime()}开始更新热搜数据")

        ts = time.strftime("%Y-%m-%d %X")
        for i in content:
            cursor.execute("insert into hotsearch(dt,content) values(%s,%s)", (ts, i))

        db.commit()
        db.close()




if __name__ == '__main__':
    update_hot()
