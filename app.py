

from flask import Flask, request
# 从flask类创建一个app对象
# __name__ :代表当前app.py的模块
# 1 出现bug，可以帮助快速定位
# 2 对于寻找模板文件，有一个相对路径
app = Flask(__name__)


# 创建一个路由和视图函数的映射  / 根路由
# https://www.baidu.com
# /home/user/xx  类似路径
@app.route('/')    # 定义一个路由的装饰器
def index():

    return "222"

# 1debug模式： 社区版在运行里，run函数加debug=true
# 开发时候，发生bug，开启debug模式，在浏览器就可以看的信息

# 2.修改host：
# 主要作用，让其他电脑，访问我的电脑，flask项目

# 修改端口：主要作用，如果5000端口被占用，访问其他端口


# url: //www.qq.com:/path
# url 与视图  path与视图


# 加自己的配置，在5000端口号直接/profile就能看到内容
@app.route("/profile")
def profile():

    return "我是个人中心"


# 后面直接加路径
@app.route("/profile/list")
def lists():

    return "个人中心列表"


# 带参数的url 参数形式<> 在后面传对应的数值
@app.route("/blog/<blog_id>")
def blog_url(blog_id):

    return "你访问的博客是：%s" % blog_id


# 将参数固定为int类型，也可以改其他类型，注意路径要和其他的不一致
@app.route("/blogs/<int:blog_id>")
def blog_urls(blog_id):

    return "你访问的博客是：%s" % blog_id


# 查询字符串的方式传参
# /book/list  返回第一页的数据
# /book/list?page=2 返回第二页的数据
@app.route('/book/list')
def book_list():

    # arguments:参数
    # request.args 类字典的类型   默认值第一页，类型是int
    page = request.args.get("page", default=1, type=int)

    return f"你获取的是第{page}页的图书列表"


if __name__ == '__main__':

    app.run(debug=True)

