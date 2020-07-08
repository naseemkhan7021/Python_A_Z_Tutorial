#Importing flask module in the projet is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app=Flask(__name__)

# the route() function of the Flask class is a decorator,
# which tells the appliction which URL should call
# the associated function.
@app.route('/')
# '/' URL is bound with hello_world() function.

def hellow_world():
    return "Hello_world"



# main driver fungtion

if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the locla development server.
    app.run()
