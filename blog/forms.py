from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField




#forms in flask

class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Submit')



class AddForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    slug = StringField(label='Slug', validators=[DataRequired()])
    content = TextAreaField(label='Content', validators=[DataRequired()])
    submit = SubmitField(label='Post')
