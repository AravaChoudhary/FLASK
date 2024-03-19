#Application routing means mapping the URLs to a specific function that handles the logic for that URL.
from flask import Flask
app = Flask(__name__)
#Define a route with a Dynamic Parameter 'id' of type integer
@app.route('/post/<int:id>')
def show_post(id):
    #Returning the String with the ID
    return f'This POST has the ID : {id}'

#Define a route with a Dynamic Parameter 'username' of type string
@app.route('/user/<username>')
def show_user(username):
    #Returning the String with the username
    return f'This User has the username : {username}'

#Define a route for "/hello" endpoint
@app.route('/hello')
def hello():
    #Returning the String "Hello World"
    return "Hello World"

#Define the default route for the root URL "/"
@app.route('/')
def index():
    #Returning the String "Hello World"
    return "HomePage of this Application"

if __name__ == '__main__':
    app.run(debug=True)