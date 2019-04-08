from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("url for", url_for('index'))
    return "hello world!"


@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    user url_for函数
    :return:
    """
    return url_for('login', user_id=1)


@app.route('/login/<int:user_id>/', methods=['GET', 'POST'])
def login(user_id):
    """
    login
    :param user_id:
    :return:
    """
    print(user_id)
    return "login"


if __name__ == '__main__':
    app.run()
