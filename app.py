from flask import Flask
from flask_wtf.csrf import CSRFProtect 
from blueprint.general import app as general
from blueprint.user import app as user
from blueprint.admin import app as admin
import connfig
from extention import db
from flask_login import LoginManager
from models.user import User

app=Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)


app.config["SQLALCHEMY_DATABASE_URI"]= connfig.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY']= connfig.SECRET_KEY

csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)
# اتصال db به اپ
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)








