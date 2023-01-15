# HEALTH SCHEDULING SYSTEM

#### Video Demo:  https://youtu.be/83H9rf1PVRs

#### Description

# introduction
This is a simple flask app derived for  previous problem sets that have helped me build this.
This is meant to be a system whereby an administrator creates 
schedules whereby doctors and patients are given an appointed time
and room for which the services are taken care off

## Technologies used
1. Python for the backend 
#### app.py

```
app.py is the main flask entry file
it contains all the routes including
    -> schedules
    -> dashboard
    -> doctors
    -> patients
    -> rooms
    -> data
*
```

#### database.db

```
The entire databse of the project with more details of the entire databse in
database.sql
```

#### utilities.py

```
some code from the previous problem set that i used in this project
```

#### database.sql

```
The entire schema for the database
```

## static folder

### images folder

```
All the images used in the entire project
```

### script folder

```
All the javascript code used in the project
```

#### style folder

```
All the stylesheets used inside the project
```

## templates folder

1. dashboard.html -> A summary page for all the data in the system

<!--  -->

2. data.html -> Al the data is presented and added in this interface

> There are three types of data in the entire project
>
> 1. Doctors
> 2. Patients
> 3. Rooms
>    Each of these data is also represneted in the database
>    as follows

```
CREATE TABLE people 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
firstname TEXT NOT NULL,
lastname TEXT,
username TEXT NOT NULL,
gender TEXT DEFAULT female,
email TEXT,
phone TEXT,
blood TEXT,
password TEXT NOT NULL);

CREATE TABLE doctors
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
firstname TEXT NOT NULL,
lastname TEXT,
username TEXT NOT NULL,
gender TEXT DEFAULT female
);

CREATE TABLE patients
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
firstname TEXT NOT NULL,
lastname TEXT,
username TEXT NOT NULL,
gender TEXT DEFAULT female
);

CREATE TABLE rooms
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT  
);

CREATE TABLE schedules
(id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_id INTEGER,
doctor_id INTEGER,
dt DATE,
hour INTEGER,
minute MINUTE  
);
```

3. index.html -> main homepage
>This is where everything begins including where
>the user is first directed when we firts enter the site

4. issue.html -> equal to apology.html
> This is used in times of errors
> it is useful to generate custom error interfaces

5. layout.html -> the components loaded before login
> This actually only applies only to index html
> it gives the header tags for the html,
> the title
> and the navbar
6. login.html -> login page
> The user keys in previously registered details

7. register.html -> signup page
> the user eneters their data into the database

8. schedules.html -> modify schedules page
> Enter scheule data into the database
> Patient _id
> doctor id
> timestamp
9. template.html -> the components loaded after login
> navbar for when user is logged in

## Process

A user creates  an account by registering after which 
the databse is ppulated with their data
A session is used 
and i have defined in three sessions for the sake of profile credentials
that is
1. username
2. firstname
3. lastname

mostly just for the sake of the navbar

# ways it can be improved
It is very buggy even though it andles it functionalities very well
I ran out of time due to the holidays and very long semester at school
hopefully new features can be implemented
like 

