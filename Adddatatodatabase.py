import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattedance-default-rtdb.firebaseio.com/"
})

ref=db.reference("Students")

data={
    "153":
        {
            "name":"SRIRAM",
            "major":"AI&DS",
            "starting_year":2020,
            "total_attendance":0,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2023-01-29 00:54:34"
        },
    "506":
        {
            "name":"TONY",
            "major":"AI&DS",
            "starting_year":2020,
            "total_attendance":0,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2023-01-29 00:54:34"
        },
    "115":
        {
            "name":"DHINESH",
            "major":"AI&DS",
            "starting_year":2020,
            "total_attendance":0,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2023-01-29 00:54:34"
        },
    "144":
        {
            "name":"RISHI",
            "major":"AI&DS",
            "starting_year":2020,
            "total_attendance":0,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2023-01-29 00:54:34"
        },
    "authorised":
        {
            "last_detected_time":"2023-01-29 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)