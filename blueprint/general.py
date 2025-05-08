from flask import Blueprint

app=Blueprint("general",__name__)

@app.route("/")
def main():
    return"<p>This is main page</p>"


@app.route("/about")
def about():
    return"<p>about us</p>"
