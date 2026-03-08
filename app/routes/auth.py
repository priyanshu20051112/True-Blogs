from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app.models import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        email = request.form.get("email").strip().lower()

       
        if not username or not email or not password:
            flash("Please fill all the fields", "error")
            return redirect(url_for('auth.register'))

       
        if User.query.filter_by(username=username).first():
            flash("Username already taken", "error")
            return redirect(url_for('auth.register'))

       
        if User.query.filter_by(email=email).first():
            flash("Email already exists, try again", "error")
            return redirect(url_for('auth.register'))

       
        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash("You registered successfully. You can now log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        user = User.query.filter_by(username=username).first()

        if not user:
            flash('User not found. Please register first.', 'error')
            return redirect(url_for('auth.login'))

        if user.check_password(password):
            session['user'] = user.id  
            flash("Successfully logged in", "success")
            return redirect(url_for('blog.home'))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('auth.login'))

    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.clear()
    flash("Successfully logged out", "success")
    return redirect(url_for('auth.login'))
