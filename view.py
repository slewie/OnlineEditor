from app import app
from flask_login import login_required, logout_user
from flask import redirect, render_template


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def index():
    return render_template('index.html')