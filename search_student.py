from sqlalchemy.orm import Session
from models import Student, engine


last_name = input("Введите фамилию студента: ")

with Session(engine) as session:
    
    students = session.query(Student).filter_by(last_name=last_name).all()

    if students:
        for student in students:
            print(
                student.last_name,
                student.first_name,
                student.faculty,
                student.course,
                student.grade
            )
    else:
        print("Студент не найден")
