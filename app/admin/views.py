# 3rd party imports
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

# Local imports
from app.admin import admin
from app.admin.forms import DepartmentForm
from app import db
from app.models import Department


def check_admin():
    """
    Prevent non-admins from accessing the page

     Return: 403 error

    """
    if not current_user.is_admin:
        abort(403)


@admin.route('departments', methods=['Get', 'POST'])
@login_required
def list_departments():
    """
    List of all departments

    return a rendered template of departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title='Departments')


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():

        department = Department(name=form.name.data)  # Todo add a  description parameter

        try:
            # add a department to the database
            db.session.add(department)
            db.session.commit()
            flash('The new department have been successfully added !')
        except :
            flash('Error: department name already exists.')

        return redirect(url_for('admin.list_departments'))

    return render_template('admin/departments/department.html', action='Add',
                           add_department=add_department,
                           form=form,
                           title='Add Department')


@admin.route('/department/edit/<int:department_id>', methods=['POST', 'GET'])
@login_required
def edit_department(department_id):
    '''
    Edit a department

    '''

    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    add_department = False

    department = Department.query.get_or_404(department_id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        # department.description = form.description.data  # ToDo description later
        db.session.commit()
        flash('You have successfully edited the department.')

        return redirect(url_for('admin.list_departments'))

    form.name.data = department.name
    # form.description.data = department.description #Todo later

    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:department_id>', methods=['GET', 'POST'])
@login_required
def delete_department(department_id):
    """
    Delete a department from the database

    """
    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    flash('The department have been successfully deleted !')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")
