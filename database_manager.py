from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Student, engine
import csv

class DatabaseManager:
    def __init__(self, engine):
        self.engine = engine

    def insert_student(self, last_name, first_name, faculty, course, grade):
        with Session(self.engine) as session:
            student = Student(
                last_name=last_name,
                first_name=first_name,
                faculty=faculty,
                course=course,
                grade=int(grade)
            )
            session.add(student)
            session.commit()
            return student.id

    def select_students(self, faculty=None):
        with Session(self.engine) as session:
            query = session.query(Student)

            if faculty is not None:
                query = query.filter(Student.faculty == faculty)

            students = query.all()

            return [
                {
                    "id": student.id,
                    "last_name": student.last_name,
                    "first_name": student.first_name,
                    "faculty": student.faculty,
                    "course": student.course,
                    "grade": student.grade
                }
                for student in students
            ]
            
    def select_students_below_30(self, course):
        with Session(self.engine) as session:
            students = session.query(Student).filter(
                Student.course == course,
                Student.grade < 30
            ).all()

            return [
                {
                    "id": student.id,
                    "last_name": student.last_name,
                    "first_name": student.first_name,
                    "faculty": student.faculty,
                    "course": student.course,
                    "grade": student.grade
                }
                for student in students
            ]

    def average_grade_by_faculty(self, faculty):
        with Session(self.engine) as session:
            average = session.query(
                func.avg(Student.grade)
            ).filter(
                Student.faculty == faculty
            ).scalar()

            return average
        
        
    def import_from_csv(self, filename):
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            with Session(self.engine) as session:
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
                
    def get_unique_courses(self):
        with Session(self.engine) as session:
            courses = session.query(Student.course).distinct().all()

            return [course[0] for course in courses]