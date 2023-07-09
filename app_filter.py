
from flask import Flask, render_template
# render_template模板
from datetime import datetime


app = Flask(__name__)


# 自定义的时间过滤器函数 传入value值， 默认参数不需要
def datetime_format(value, format="%Y年-%d月-%m日 %H:%M"):

    return value.strftime(format)


# app对象的添加模板过滤器的方法
app.add_template_filter(datetime_format, "dformat")


class User:

    def __init__(self, username, email, page_name):

        self.username = username
        self.email = email
        self.page_name = page_name


@app.route('/')
def first_page():

    return "学习flask首页"


@app.route('/filter')
def filter_demo():

    user = User(username="lcy", email="lcy@qq.com", page_name="flask学习首页")
    # 传入实例的对象。变量，就是user.username, 或者user.email  | 管道符 加length传入的字符长度
    my_time = datetime.now()  # 获取现在的时间,对象。传给模板
    return render_template("filter.html", user=user, my_time=my_time)


@app.route('/control')
def control_statement():

    age = 17
    # if判断 {% %} 结尾要有{% endif %}  for循环也是这样，但是没有break，循环完全

    books = [
        {"name": "三国演义",
         "author": "罗贯中"},
        {
            "name": "水浒传",
            "author": "施耐庵"
        }
    ]
    return render_template("control.html", age=age, books=books)


@app.route("/child1")
def child1():

    return render_template("child1.html")


@app.route("/child2")
def child2():

    return render_template("child2.html")


@app.route('/static')
def static_demo():

    return render_template("static.html")


if __name__ == '__main__':

    app.run(debug=True)
