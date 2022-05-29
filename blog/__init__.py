from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5



app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # database configuration
app.config['SECRET_KEY'] ='some very complex words' # flask-WTF configuration

bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)


from blog import routes