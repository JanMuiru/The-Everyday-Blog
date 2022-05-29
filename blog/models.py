from blog import db
from datetime import datetime 







#database model in flask
class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    title = db.Column(db.String(length=30), nullable=False)
    author = db.Column(db.String(length=50), nullable=False)
    slug = db.Column(db.String(length=50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

