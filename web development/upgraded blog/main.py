import smtplib
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/de75f5abaf7cf39fff4c")
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    data = request.form
    if request.method == "POST":
        with smtplib.SMTP('smtp.gmail.com') as connectiom:
            connectiom.starttls()
            connectiom.login("newtonde97@gmail.com", "blwrejwokdapjclz")
            connectiom.sendmail(
                from_addr="newtonde97@gmail.com",
                to_addrs="newtonnarzary28@gmail.com",
                msg=f'Subject:New Message\n\nname:{data["name"]}\nemail:{data["email"]}\nphone:{data["phone"]}\nmessage:{data["message"]}'
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post["id"] == index:
            requested_post = post
            return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
