from Flask_project1.app import app

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is an informational page.'

@app.route('/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'The sum of {a} and {b} is {a + b}.'

@app.route('/reverse/<string:word>')
def reverse(word):
    if len(word) > 0:
        return f'Original word: {word}. Reversed word: {word[::-1]}'
    else:
        return f'Введите текст для переворота.'

@app.route('/user/<string:name>/<int:age>')
def user(name, age):
    if age >= 0:
        return f'Hello, {name}. You are {age} years old.'
    else:
        return f'Возраст должен быть больше "0".'
