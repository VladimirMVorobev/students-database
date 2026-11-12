from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Student, engine

faculty = input("Введите факультет: ")

with Session(engine) as session:
    average = session.query(func.avg(Student.grade)).filter(
        Student.faculty == faculty
    ).scalar()

    if average is not None:
        print(f"Средний балл: {average:.2f}")
    else:
        print("Факультет не найден")