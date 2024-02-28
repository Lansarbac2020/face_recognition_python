import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendanceschools-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "156730":
        {
            "name": "Kadidia Traore",
            "major": "Civil Engineering",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2023-12-11 00:32:45"

        },
    "267340":
        {
            "name": "Bacoro Lansar",
            "major": "Computer Engineering",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "M",
            "year": 2,
            "last_attendance_time": "2023-12-09 15:30:45"

        },
    "321798":
        {
            "name": "Barack Obama",
            "major": "Ex-President",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "VG",
            "year": 3,
            "last_attendance_time": "2023-05-11 13:32:35"

        },
    "345500":
        {
            "name": "Mohamed L Cisee",
            "major": "Civil-Eng",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-05-11 08:32:35"

        }

}

for key, value in data.items():
    ref.child(key).set(value)

