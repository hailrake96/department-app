# 3rd party imports
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

# Local imports
from . import auth
# import app.auth as auth
from app.auth.forms import LoginForm, RegistrationForm
from app import db
from app.models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        employee = Employee(username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add employee to the database
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered! You may log in now.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm

    if form.validate_on_submit():

        # check whether employee exists in database and whether
        # the password entered mathes the password in the database
        employee = Employee.quert.filter_by(email=form.email.data).fisrt()
        if employee is not None and employee.verify_password(
                form.password.data):
            # log employee in
            login_user(employee)

            # redirec to the dashboard page after login
            return redirect(url_for('home.dashboard'))

    # when login details are incorrect
    else:
        flash('Invalid email or password')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
