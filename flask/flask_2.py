#Importing flask module in the projet is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
app=Flask(__name__)

@app.route('/')
# '/' URL is bound with hello_world() function.
def hellow_world():
    return "Hello_There"

@app.route('/hellow/<name>')
def hellow_name(name):

    return 'hellow %s!' % name

if __name__ == '__main__':
    app.run()
