from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "hellooooooo"
@app.route("/home")
def home():
    return "welcome to my home page"
@app.route("/home about")
def about():
    return "LTTE"
if(__name__=="__main__"):
 app.run(debug=True)