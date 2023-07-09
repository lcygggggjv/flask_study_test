from flask import Flask, render_template
# 导入读取的模块方法render_template

app = Flask(__name__)


class User:

    def __init__(self, username, email):

        self.username = username
        self.email = email


@app.route('/')
def get_class_variable():
    # python的user类，对象实例化，传入形参
    # html文件里获取，要是这里实例的对象user 获取变量就是 user.username 一样的
    user = User(username="lcy", email="lcy@qq.com")
    person = {
        "age": 24,
        "city": "hz"
    }
    # 传进去实例的对象，html通过user.usaername获取值 字典等类型，也是直接传，然后python取法一致， person["code"] 字典也可以person.code 最多
    return render_template("index.html", user=user, person=person)


@app.route('/')
def study():
    # 使用读取模板的方法render_template，传入文件路径
    return render_template("index.html")


@app.route('/blog/<blog_id>')
def blog_detail(blog_id):

    # blog_id传的数字，传给了前面的html文件 对应的html文件的变量名一致，{{blog_id}}花括号 这里有几个变量，对应html相同
    return render_template("blog_detail.html", blog_id=blog_id, username="lcy")


if __name__ == '__main__':

    app.run(debug=True)

