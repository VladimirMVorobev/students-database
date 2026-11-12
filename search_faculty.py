from sqlalchemy.orm import Session
from models import Student, engine

faculty = input("Введите факультет: ")

with Session(engine) as session:
    students = session.query(Student).filter(
        Student.faculty.ilike(f"%{faculty}%")
    ).all()

    if students:
        print(f"Найдено студентов: {len(students)}")

        for student in students:
            print(
                student.last_name,
                student.first_name,
                student.faculty,
                student.course,
                student.grade
            )
    else:
        print("Студенты не найдены")
