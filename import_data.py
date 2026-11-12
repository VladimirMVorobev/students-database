import csv
from sqlalchemy.orm import Session
from models import Student, engine

with open("students.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    with Session(engine) as session:
        for row in reader:
            student = Student(
                last_name=row["Фамилия"],
                first_name=row["Имя"],
                faculty=row["Факультет"],
                course=row["Курс"],
                grade=int(row["Оценка"])
            )
            session.add(student)
        session.commit()