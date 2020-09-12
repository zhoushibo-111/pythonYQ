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
def get_baidu_head():
    browser = webdriver.Chrome(r'C:\chrome\chromedriver.exe')
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner"
    wait = WebDriverWait(browser, 10)
    browser.get(url)
    time.sleep(1)

    but = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div[1]/div/div/div[2]')

    content = [i.text for i in but]
    return content


def update_yq():
    content = get_baidu_head()
    print(f"{time.asctime()}开始插入头部数据")
    ts = time.strftime("%Y-%m-%d %X")

    cursor.execute("insert into total(xy_Diag,no_symptom,xy_suspect,xy_illness,lj_Diag,jwsr,lj_cure,dead,dt) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(content[0],content[1],content[2],content[3],content[4],content[5],content[6],content[7],ts))

    db.commit()
    db.close()



if __name__ == '__main__':
    update_yq()