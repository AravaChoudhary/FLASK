from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, I am Starting my Journey with Flask and It's going great"

# For running this app, we have to call the run method
if __name__ == "__main__":
    app.run(debug = True)
    