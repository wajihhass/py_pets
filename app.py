
from petfax import create_app
app = create_app()








'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index2():
    return 'Hello World!!!'

    @app.route('/pets')
    def pets():
        return 'This is where we keep our pets info'

@app.rout('/fruit/<int:f>')
def printFruit(f):
    print(f)
    return str(f)
    '''