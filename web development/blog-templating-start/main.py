from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_data)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog in blog_data:
        if blog['id'] == index:
            requested_post = blog
            return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)
