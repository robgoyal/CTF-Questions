import os
import re
import uuid

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_apscheduler import APScheduler
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Create directory for contact forms
os.makedirs("app/complaints")

# Initialize app and extension applications
app = Flask(__name__)
app.secret_key = '<REPLACE_SECRET_KEY>'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

engine = create_engine("sqlite:///app.db")
con = engine.connect()

# Create Tables
con.execute(text("DROP TABLE IF EXISTS users;"))
con.execute(text("DROP TABLE IF EXISTS grades;"))
con.execute(text("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL, password TEXT NOT NULL);"""))
con.execute(text("""CREATE TABLE grades (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL, courseId TEXT NOT NULL,
                    grade INTEGER NOT NULL, notes TEXT);"""))

# Create users
with open("passwords.txt") as f:
    passwords = [password.strip() for password in f.readlines()]

query = text("INSERT INTO USERS (username, password) VALUES(:username, :password)")
seeded_users = (
    {"username": "kate", "password": '<REPLACE_KATE_PASSWORD>'},
    {"username": "adam", "password": '<REPLACE_ADAM_PASSWORD>'},
    {"username": "jess", "password": '<REPLACE_JESS_PASSWORD>'},
)
for seeded_user in seeded_users:
    con.execute(query, seeded_user)

# Insert flag
with open("flag.txt") as f:
    flag = f.read()

# Insert grades
query = text("INSERT INTO grades (username, courseId, grade, notes) VALUES(:username, :courseId, :grade, :notes)")
seeded_grades = (
    {"username": "kate", "courseId": "101", "grade": "80", "notes": "Great success!"},
    {"username": "kate", "courseId": "102", "grade": "56", "notes": "Almost a fail..."},
    {"username": "adam", "courseId": "101", "grade": "75", "notes": "Spot on!"},
    {"username": "adam", "courseId": "102", "grade": "98", "notes": "Holy cow ... mooooooo"},
    {"username": "jess", "courseId": "101", "grade": "69", "notes": "very niceeeee)"},
    {"username": "jess", "courseId": "102", "grade": "80", "notes": flag},
)
for seeded_grade in seeded_grades:
    con.execute(query, seeded_grade)

# Commit all changes
con.commit()

# Scheduled job
@scheduler.task('cron', id='process_contact_forms', minute='*')
def process_contact_forms():
    admin = con.execute(text('SELECT id, username FROM users WHERE username = "jess"')).fetchone()
    with app.test_request_context("/"), app.test_client() as client:
        login_user(User(admin[0], admin[1]))
        forms = os.listdir("app/complaints")
        for form in forms:
            formpath = os.path.join("app/complaints", form)
            with open(formpath, "r") as f:
                formdata = f.read()
                urls = re.findall("(?P<url>https?://[^\s]+)", formdata)
                for url in urls:
                    client.get(url)
        logout_user()

# Flask login loader callbacks
class User(UserMixin):
    def __init__(self, _id, username):
        self.id = _id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    result = con.execute(text('SELECT id, username FROM users WHERE id = :user_id'), {"user_id": user_id}).fetchone()
    return User(result[0], result[1]) if result else None

# Logout view
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for('login'))


# Login view
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':

        username_error = ''
        password_error = ''

        # Get form request parameters
        username = request.values.get('username', '').strip()
        password = request.values.get('password', '').strip()

        # Check if username or password is empty
        if len(username) == 0:
            username_error = "Username field cannot be empty."
        if len(password) == 0:
            password_error = "Password field cannot be empty."

        if username_error == '' and password_error == '':
            username_query = text("SELECT id, username, password FROM users WHERE username = :username")
            result = con.execute(username_query, {"username": username}).fetchone()
            if result is None:
                username_error = "No account found with that username."
            else:
                if result[2] != password:
                    password_error = "Password not valid."
                else:
                    user = User(result[0], result[1])
                    login_user(user)
                    return redirect(url_for('index'))
        return render_template('login.html', username_error=username_error, password_error=password_error)
    else:
        return render_template('login.html')

# Register view
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username_error = ''
        password_error = ''
        confirmp_error = ''

        # Get form request parameters
        username = request.values.get('username', '').strip()
        password = request.values.get('password', '').strip()
        confirmp = request.values.get('confirm_password', '').strip()

        # Check if username or password is empty
        if len(username) == 0:
            username_error = "Username field cannot be empty."
        if len(password) == 0:
            password_error = "Password field cannot be empty."
        if len(confirmp) == 0:
            confirmp_error = "Please confirm password."

        # Check if user exists
        if username_error == '' and password_error == '' and confirmp_error == '':
            username_query = text("SELECT id, username, password FROM users WHERE username = :username")
            result = con.execute(username_query, {"username": username}).fetchone()
            if result:
                username_error = "Username already exists."
            else:
                if password != confirmp:
                    confirmp_error = "Password did not match."
                else:
                    insert_user_query = text("INSERT INTO USERS (username, password) VALUES(:username, :password)")
                    con.execute(insert_user_query, {"username": username, "password": password})
                    con.commit()
                    flash("Registered.")
                    return redirect(url_for('login'))
        return render_template('register.html', username_error=username_error, password_error=password_error, confirm_password_error=confirmp_error)
    else:
        return render_template('register.html')

# Change password view
@app.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():

    password_error = ''
    confirmp_error = ''

    # Get form request parameters
    password = request.values.get('password', '').strip()
    confirmp = request.values.get("confirm_password", '').strip()

    # Check if password is empty
    if len(password) == 0:
        password_error = "Password field cannot be empty."
    if len(confirmp) == 0:
        confirmp_error = "Please confirm password."

    # Check if user exists
    if password_error == '' and confirmp_error == '':
        if password != confirmp:
            confirmp_error = "Password did not match."
        else:
            update_user_query = text("UPDATE USERS SET password = :password WHERE id = :id")
            con.execute(update_user_query, {"password": password, "id": current_user.id})
            con.commit()
            flash("Password Updated")
            logout_user()
            return redirect(url_for('login'))
    return render_template('change-password.html', password_error=password_error, confirm_password_error=confirmp_error)

# Add a grade view
@app.route("/add-grade", methods=["GET", "POST"])
@login_required
def add_grade():
    courseid_error = ''
    grade_error = ''
    notes_error = ''

    if request.method == "POST":
        if request.values.get("submit", '') == "Cancel":
            return redirect(url_for("index"))

        courseid = request.values.get("courseid", '').strip()
        grade = request.values.get("grade", '').strip()
        notes = request.values.get("notes", '').strip()

        if len(courseid) == 0:
            courseid_error = "Please enter a course ID."
        if len(grade) == 0:
            grade_error = "Please enter a grade."
        try:
            grade = int(grade)
        except:
            grade_error = "Grade must be a number."
        if isinstance(grade, int) and grade not in range(0, 101):
            grade_error = "Grade must be between 0 and 100."

        if courseid_error == "" and grade_error == "":
            course_query = text("SELECT courseId, grade, notes FROM grades WHERE courseId = :courseid")
            results = con.execute(course_query, {"courseid": courseid}).fetchone()
            if results:
                update_grade_query = text("UPDATE GRADES SET grade = :grade, notes = :notes WHERE (username = :username AND courseId = :courseid)")
                con.execute(update_grade_query, {"username": current_user.username, "grade": grade, "courseid": courseid, "notes": notes})
                con.commit()
                flash("Course already exists. Update the grade and notes.")
                return redirect(url_for("index"))
            else:
                insert_grade_query = text("INSERT INTO grades (username, courseId, grade, notes) VALUES(:username, :courseId, :grade, :notes)")
                con.execute(insert_grade_query, {"username": current_user.username, "grade": grade, "courseId": courseid, "notes": notes})
                con.commit()
                flash("Added grade")
                return redirect(url_for("index"))
        return render_template("add-grade.html", grade=grade, courseid=courseid, notes=notes, courseid_error=courseid_error, grade_error=grade_error, notes_error=notes_error)
    else:
        return render_template("add-grade.html")

# Contact view
@app.route("/contact", methods=["GET", "POST"])
@login_required
def contact():
    message = ''
    message_error = ''

    if request.method == "POST":
        if request.values.get("submit", "").strip() == "Cancel":
            return redirect(url_for("index"))

        message = request.values.get("message", "").strip()
        if len(message) == 0:
            message_error = "Please enter a message."
        elif len(message) > 1000:
            message_error = "Keep message less than 1000 characters."
        if message_error == "":
            with open(os.path.join("app", "complaints", str(uuid.uuid4())), "w") as f:
                f.write(message)
            flash("Message Sent.")
            return redirect(url_for("index"))
        return render_template("contact.html", message=message, message_error=message_error)
    else:
        return render_template("contact.html")

# Index view
@app.route('/', methods=["GET"])
@login_required
def index():
    if request.values.get("action") == "delete" and request.values.get("id") != "":
        delete_query = text("DELETE FROM GRADES WHERE (id = :id AND username = :username)")
        result = con.execute(delete_query, {"id": request.values.get("id", ""), "username": current_user.username})
        if result.rowcount == "0":
            flash("Note does not exist.")
        else:
            flash("Note deleted.")
            con.commit()
    grades_query = text("SELECT id, courseId, grade, notes FROM grades WHERE username = :username")
    grades = con.execute(grades_query, {"username": current_user.username})
    return render_template('index.html', grades=grades)
