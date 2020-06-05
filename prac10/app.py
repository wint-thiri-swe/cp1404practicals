from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return "Hello {}".format(name)


# def temperature_converter():
#     celsius = float(input("Enter degree: "))
#     fahrenheit = celsius * 9.0 / 5 + 32
#     return fahrenheit


@app.route('/f')
@app.route('/f/<celsius>')
def temperature_converter(celsius=''):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return '{:.2f} C  is  {:.2f} F'.format(float(celsius), fahrenheit)


if __name__ == '__main__':
    app.run()
