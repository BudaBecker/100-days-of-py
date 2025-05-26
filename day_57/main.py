from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", data = blog_data)

@app.route("/post/<id>")
def post(id):
    
    post_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", data = post_data[int(id) - 1])

if __name__ == "__main__":
    app.run(debug=True)
