from sqlalchemy.orm import Session
from models import Student, engine

with Session(engine) as session:
    courses = session.query(Student.course).distinct().all()

    for course in courses:
        print(course[0])