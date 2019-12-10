# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    # desciption = StringField('Description',validators=[DataRequired]) # ToDO make that on Future
    submit = SubmitField('Submit')
