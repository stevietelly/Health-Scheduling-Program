from functools import wraps
from flask import redirect, render_template, request, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

def render_error(message):
    return render_template("issue.html", message=message)