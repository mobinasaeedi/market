from flask import Blueprint

app=Blueprint("admin",__name__)

@app.route("/admin")
def admin():
    return("<p>This is admin page</p>")