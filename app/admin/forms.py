# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField


# Local imports
from app.models import Department,Employee


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    # desciption = StringField('Description',validators=[DataRequired]) # ToDO make that on Future
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department_name = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    # role = QuerySelectField(query_factory=lambda: Department.query.all(),
    #                               get_label="name")
    submit = SubmitField('Submit')

