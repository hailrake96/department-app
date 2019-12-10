from flask import render_template, abort
from flask_login import login_required, current_user

from app.home import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """
    Return rendered admin-user page.

    After checking out admin rights render admin-user page.
    """

    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title='Dashboard')
