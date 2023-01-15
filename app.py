from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from cs50 import SQL
from utilities import render_error, login_required
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config.update(SESSION_SAME_SITE="None", SESSION_COOKIE_SECURE=True)
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Main Index Page"""
    session.update()

    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    "Register Page"
    if request.method == "GET":
        return render_template("register.html", name=False, id=False, bio=False, pas=False)
    if request.method == "POST":
       
        title = request.form.get("title")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")

        if not title or not firstname or not lastname:
            return render_template("register.html", name=True, id=False, bio=False, pas=False)

        gender = request.form.get("gender")
        email = request.form.get("email")
        phone = request.form.get("phone")

        if not gender or not email or not phone:
            return render_template("register.html", name=False, id=True, bio=False, pas=False)

        dob = request.form.get("dob")
        blood = request.form.get("blood")
        height = request.form.get("height")
        weight = request.form.get("weight")

        username =  request.form.get("username")
        password =  request.form.get("pass")
        conpass =  request.form.get("conpass")

        if not dob or not height or not weight or not username or not password or not conpass or not blood:
            return render_template("register.html", name=False, id=False, bio=True, pas=False)

        # If passwords dont match
        if  conpass != password:
            return render_template("register.html", name=False, id=False, bio=False, pas=True)

        # Check if username exists
        get_usernames = db.execute("SELECT username FROM people")
        usernames = []
        for i in get_usernames:
            usernames.append(i['username'])
        if username in usernames:
            return render_template("register.html", name=False, id=False, bio=False, pas=False, user=True)

        # hash password
        hashpass = generate_password_hash(password)

        # Add new user to database
        db.execute("INSERT INTO people (title, firstname, lastname, username, gender, email, phone, blood, hashpass, dob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        title, firstname, lastname, username, gender, email, phone, blood, hashpass, dob)

        # Create Session
        user_id = db.execute("SELECT id FROM people WHERE title = ? AND email = ? AND hashpass = ? AND  gender = ? AND blood = ?"
        , title, email, hashpass, gender, blood)

        session['user_id'] = user_id[0]['id']
        session['username'] = username
        session['firstname'] = firstname
        session['lastname'] = lastname

    return render_template("index.html")

@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via GET
    if request.method == "GET":  
        return render_template("login.html")
    else:
        username =  request.form.get("username")
        password =  request.form.get("password")

        # validation
        if not username and not password:
            return render_template("login.html", details=True)

        # check if user exsits
        res = db.execute("SELECT id, hashpass, firstname, lastname FROM people WHERE username = ?", username)

        if len(res) != 1:
            return render_template("login.html", user=True)
        
        # confirm password
        if not check_password_hash(res[0]["hashpass"], request.form.get("password")):
            return render_template("login.html", password=True)
        
        session['user_id '] = res[0]['id']
        session['firstname'] = res[0]['firstname']
        session['lastname'] = res[0]['lastname']
        session['username'] = username

    return render_template("index.html")

@app.route("/data")
@login_required
def data():
    doctors = db.execute("SELECT * FROM doctors")
    patients = db.execute("SELECT * FROM patients")
    rooms = db.execute("SELECT * FROM rooms")

    stats = {"doctors": 0, "patients": 0, "female_patients": 0, "male_patients": 0, "male_doctors": 0, "female_doctors": 0, "total_rooms": 0}
    stats['doctors'] = db.execute("SELECT COUNT(id) FROM doctors")[0]['COUNT(id)']
    stats["patients"] = db.execute("SELECT COUNT(id) FROM patients")[0]['COUNT(id)']
    stats["total_rooms"] = db.execute("SELECT COUNT(id) FROM rooms")[0]['COUNT(id)']

    stats["female_doctors"] = db.execute("SELECT COUNT(id) FROM doctors WHERE gender LIKE ?", "female")[0]['COUNT(id)']
    stats["male_doctors"] = db.execute("SELECT COUNT(id) FROM doctors WHERE gender LIKE ?", "male")[0]['COUNT(id)']

    stats["female_patients"] = db.execute("SELECT COUNT(id) FROM patients WHERE gender LIKE ?", "female")[0]['COUNT(id)']
    stats["male_patients"] = db.execute("SELECT COUNT(id) FROM patients WHERE gender LIKE ?", "male")[0]['COUNT(id)']
    return render_template("data.html", doctors=doctors, patients=patients, rooms=rooms, stats=stats)

@app.route("/dashboard")
@login_required
def dashboard():
    docs = db.execute("SELECT COUNT(id) FROM doctors")[0]['COUNT(id)']
    pats = db.execute("SELECT COUNT(id) FROM patients")[0]['COUNT(id)']
    rooms = db.execute("SELECT COUNT(id) FROM rooms")[0]['COUNT(id)']

    return render_template("dashboard.html", docs=docs, pats=pats, rooms=rooms)

@app.route("/schedules", methods=["GET", "POST"])
@login_required
def schedule():
    if request.method == "GET":
        data = db.execute("SELECT * FROM schedules")
        return render_template("schedules.html", data=data)
    else:
        patient_id = request.form.get("patient")
        doctor_id = request.form.get("doctor")
        appointment = request.form.get("appointment")
        hour = request.form.get("hour")
        minute = request.form.get("minute")

        db.execute("INSERT INTO schedules (patient_id, doctor_id, dt, hour, minute) VALUES (?, ?, ?, ?, ?)",
        patient_id, doctor_id, appointment, hour, minute)
        return redirect("/schedules")

@app.route("/doctors", methods=["POST"])
@login_required
def doctor():
    title = request.form.get("title")
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    username = request.form.get("username")

    if not title or not firstname or not lastname or not gender:
        render_error("Please input all fields")
    
    db.execute("INSERT INTO doctors (title, firstname, lastname, gender, username) VALUES(?, ?, ?, ?, ?)",
    title, firstname, lastname, gender, username)
    return redirect("/data")
    
@app.route("/patients", methods=["POST"])
@login_required
def patient():
    title = request.form.get("title")
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    username = request.form.get("username")

    if not title or not firstname or not lastname or not gender:
        render_error("Please input all fields")
    
    db.execute("INSERT INTO patients (title, firstname, lastname, gender, username) VALUES(?, ?, ?, ?, ?)",
    title, firstname, lastname, gender, username)
    return redirect("/data")

    
@app.route("/room", methods=["POST"])
@login_required
def room():
    title = request.form.get("name")
    if not title:
        render_error("Please input all fields")
    db.execute("INSERT INTO rooms (title) VALUES(?)", title)
    return redirect("/data")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("issue.html"), 404