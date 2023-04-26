from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home_page():
    blogs_api_url = "https://api.npoint.io/45ad8d22103f819531d7"
    blog_response = requests.get(blogs_api_url)
    blog_data = blog_response.json()
    return render_template("index.html", posts=blog_data)


@app.route("/index.html")
def home():
    blogs_api_url = "https://api.npoint.io/45ad8d22103f819531d7"
    blog_response = requests.get(blogs_api_url)
    blog_data = blog_response.json()
    return render_template("index.html", posts=blog_data)


@app.route("/about.html")
def about_me_page():
    return render_template("about.html")


@app.route("/contact.html")
def contact_me_page():
    return render_template("contact.html")


@app.route("/post.html/<int:post_id>")
def single_post(post_id):
    blog_url = "https://api.npoint.io/45ad8d22103f819531d7"
    blog_response = requests.get(blog_url)
    blog_posts = blog_response.json()
    the_post = None

    for post in blog_posts:
        if int(post["id"]) == int(post_id):
            the_post = post
    return render_template("post.html", post=the_post)


@app.route("/form_entry", methods=["POST"])
def receive_data():
    # you can check first to see if the message is from a form
    if request.method == "POST":
        data = request.form
        name = data["username"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        msg = "Message successfully sent!"

        return f"<h1>{name} Your Message was Successfully Sent</h1>"


if __name__ == "__main__":
    app.run(debug=True)
