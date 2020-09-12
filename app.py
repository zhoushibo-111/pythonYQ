from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import utils
import baiduYiQingHead

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route('/cx')
def get_cx_data():
    data = utils.get_cx_data()
    for row in data:
        return jsonify(
            {"xy_Diag": row[1], "no_symptom": row[2], "xy_suspect": row[3], "xy_illness": row[4], "lj_Diag": row[5],
             "jwsr": row[6], "lj_cure": row[7], "dead": row[8]})


@app.route('/rs')
def get_hot_data():
    data = utils.get_hotsearch()
    list = []
    for row in data:

        list.append(row[2])

    return jsonify(
        {"content1": list[0],"content2": list[1],"content3": list[2],"content4": list[3],"content5": list[4]}
        )


@app.route('/abc')
def hello_world1():
    id = request.values.get("id")
    return f"""
    <form action="/login">
    账号<input name="name" value="{id}"><br>
    密码<input name="pwd" value="123456">
    <input type="submit">
    </form>
    """


@app.route('/login')
def hello_world2():
    name = request.values.get("name")
    pwd = request.values.get("pwd")
    return f'name={name},pwd={pwd}'


@app.route('/tem')
def hello_world3():
    return render_template("index.html")


@app.route('/ajax', methods=["get", "post"])
def hello_world4():
    name = request.values.get("name")
    age = request.values.get("age")
    # 前台给后台发送数据
    # print(f"name:{name},age:{age}")
    return "1000"


@app.route('/time')
def getTime():
    return utils.get_time()


if __name__ == '__main__':
    baiduYiQingHead.update_yq()
    app.run()
    #get_hot_data()
