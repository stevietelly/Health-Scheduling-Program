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