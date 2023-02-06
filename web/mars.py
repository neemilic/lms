from flask import Flask

app = Flask(__name__)


@app.route('/')
def a():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"

@app.route('/promotion')
def promotion():
    return '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])
@app.route('/image_mars')
def image_mars():
    return """<title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <<img src="/static/img/MARS.png">
    Вот он какая, красная планета
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
