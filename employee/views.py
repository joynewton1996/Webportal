
from flask import (Blueprint,render_template)

blueprint = Blueprint("employee", __name__, url_prefix="/employee", static_folder="../static")

@blueprint.route("/employee_login/")
def employee_login():
    """Employee login Page"""
    return render_template("employee/employee_login.html")

@blueprint.route("/employee_register/")
def employee_register():
    """Employee Register page"""
    return render_template("employee/employee_register.html")
