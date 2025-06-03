from flask import Blueprint
import models.user
import models.product

app=Blueprint("user",__name__)

@app.route("/user")
def user():
    retgit urn("<p>This is user page</p>")