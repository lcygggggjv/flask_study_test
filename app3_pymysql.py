from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from app.config import Config
from sqlalchemy import text


app = Flask(__name__)
# app.config.from_object(Config)
# mysql所在主机名
HOSTNAME = "127.0.0.1"

# MYSQL监听的端口号，默认3306
PORT = 3306

# 连接mysql的用户名，读者自己设置
USERNAME = "root"

# 连接mysql的密码，读者自己设置
PASSWORD = "123456789"

# 连接mysql数据库的名称
DATABASE = "database_learn"


app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:" \
                                        f"{PORT}/{DATABASE}?charset=utf8mb4"


# 在app.config设置好连接数据库的信息
# 然后使用SQLalchemy(app) 创建一个db 对象
# sqlalchemy 会自动读取app.config中连接数据库的信息

db = SQLAlchemy(app)

# 创建migrate对象 传入app, db2个对象
migrate = Migrate(app, db)


# !!!!!!!!   orm模型映射成表的三步
# 1  flask db init  初始化脚本，这步只需要执行一次，生成一个文件存放迁移脚本

# 用这个方法才行
# with app.app_context():
#     rs = db.session.execute(text("select 1"))
#     print(rs.fetchone())

# 上下文打开 测试连接数据库用的  现在不行了
# with app.app_context():
#     # 获取引擎连接，赋值给conn对象，执行execute
#     with db.engine.connect() as conn:
#
#         rs = conn.execute("select 1")
#
#         print(rs.fetchone())  # (1,)


class User(db.Model):

    __tablename__ = "user"
    # 表的字段,及字段类型，id主键， autoincrement自动增长 id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar null =0 nullable 表示字段不能为空
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    code = db.Column(db.String(100))
    thing = db.Column(db.String(100))
    # 和article一一对应
    # articles = db.relationship("Article", back_populates="author")

# user = User(username="lcy", password="123456")
# sql: insert user(username, password) value("lcy", "123456")


class Article(db.Model):

    __tablename__ = "article"
    # 表的字段,及字段类型，id主键， autoincrement自动增长 id   string 250个字符
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar null =0 nullable 表示字段不能为空
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 添加作者的外键  引用的到对应user表的id字段 找到对应表值  字段类型要一致sting
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 找当前这个表的字段，和user表产生 关联外键的操作  author_id 和 user——id关联
    # author = db.relationship("User", back_populates="articles") 和上面user一一对应
    # backref 自动的给user模型添加一个article的属性，用来获取文章列表
    author = db.relationship("User", backref="articles")


# article = Article(title="FLSAk学习", content="flask1222")
# article.author_id = user.id  userid 赋值给authorid
# user = User.query.get(article.author_id)
# print(article.author_id)

# # 后续增加的字段，删除字段都不会显示
# with app.app_context():
#
#     db.create_all()


@app.route('/user/add')
def add_user():
    # 创建orm对象
    user = User(username="cr7", password="777777", email="111.qq.com", signature='222', code='222')
    # 将orm对象添加到db.session中
    db.session.add(user)
    # 将db.session的改变同步到数据库里 ,提交一次事务
    db.session.commit()
    return "用户创建成功"  # 返回到页面的信息类似新增成功alert


@app.route('/user/query')
def query_user():
    # get查找；根据主键查找,1是表里的id ,id=1的对象  单条数据get  filter的多条数据
    # user = User.query.get(1)
    # print(f"{user.username}-{user.password}")
    # filter_by 查找  query对象
    users = User.query.filter_by(username="cr7")
    for user in users:
        print(user.username)
        return "数据查找成功"  # 和平时搜索一样，输入值返回结果，还有alert提示


@app.route('/user/update')
def update_user():
    # 修改表的数据 first()获取满足条件的第一个数据  [0] 切片0 ，空数据 报错 first返回null  返回user对象
    user = User.query.filter_by(username="cr7").first()
    user.password = "66666"
    db.session.commit()   # 提交事务更新数据库
    return "修改成功"


@app.route('/user/delete')
def delete_user():
    # 先查找,get方法的 生成user对象
    user = User.query.get(1)
    # 从db.session删除
    db.session.delete(user)
    # 将db.session 的修改。同步到数据库
    db.session.commit()
    return "删除成功"


@app.route('/article/add')
def article_add():

    article1 = Article(title="FLSAk学习", content="flask1222")
    article1.author = User.query.get(2)

    article2 = Article(title="Django学习", content="Django88")
    article2.author = User.query.get(2)

    # 添加session中 add_all  多个数据，添加到列表里
    db.session.add_all([article1, article2])
    # 同步数据库
    db.session.commit()
    return "文章添加成功"


@app.route('/article/query')
def article_query():
    # 根据作者的id查找
    user = User.query.get(2)
    # articles所有的对象
    for article in user.articles:
        # 查找作者所有的文章标题
        print(article.title)
    return "文章查找成功"


@app.route('/')
def hello():

    return "hello word"


if __name__ == '__main__':

    app.run(debug=True)

