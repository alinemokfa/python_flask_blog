from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Below key is only an example. This key will be replaced by an env. variable once deployed.
app.config['SECRET_KEY'] = '94557b91dc00450b6b32460246fcef8f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_blog import routes
