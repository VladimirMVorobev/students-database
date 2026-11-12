from sqlalchemy.orm import Session
from models import Student, engine
from database_manager import DatabaseManager
db = DatabaseManager(engine)

while True:

    print("=== БАЗА СТУДЕНТОВ ===")
    print("1 — Поиск по фамилии")
    print("2 — Поиск по факультету")
    print("3 — Поиск по оценке")
    print("4 — Добавить студента")
    print("5 - Студенты с оценкой ниже 30 по курсу")
    print("6 - Средний балл по факультету")
    print("7 - Список уникальных курсов")
    print("0 — Выход")

    choice = input("Выберите действие: ")
    if choice == "1":
        last_name = input("Введите фамилию: ")

        with Session(engine) as session:
            students = session.query(Student).filter(
                Student.last_name.ilike(f"%{last_name}%")
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
                
    elif choice == "2":
        faculty = input("Введите факультет: ")

        students = db.select_students(faculty)

        if students:
                print(f"Найдено студентов: {len(students)}")

                for student in students:
                    print(
                        student["last_name"],
                        student["first_name"],
                        student["faculty"],
                        student["course"],
                        student["grade"]
                    )
        else:
                print("Студенты не найдены")
                

    elif choice == "3":
        grade = int(input("Введите оценку: "))

        with Session(engine) as session:
            students = session.query(Student).filter_by(grade=grade).all()

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
                
    elif choice == "4":
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            faculty = input("Факультет: ")
            course = input("Курс: ")
            grade = int(input("Оценка: "))

            with Session(engine) as session:
                student = Student(
                    last_name=last_name,
                    first_name=first_name,
                    faculty=faculty,
                    course=course,
                    grade=grade
                )

                session.add(student)
                session.commit()

            print("Студент успешно добавлен!")  
            
    elif choice == "5":   
        course = input("Введите курс: ")

        students = db.select_students_below_30(course)

        if students:
            print(f"Найдено студентов: {len(students)}")

            for student in students:
                print(
                    student["last_name"],
                    student["first_name"],
                    student["faculty"],
                    student["course"],
                    student["grade"]
                )
        else:
            print("Студенты не найдены")      
                
    elif choice == "6":
        faculty = input("Введите факультет: ")

        average = db.average_grade_by_faculty(faculty)

        if average is not None:
            print(f"Средний балл факультета {faculty}: {average:.2f}")
        else:
            print("Факультет не найден")           
                
    elif choice == "7":
        courses = db.get_unique_courses()

        print("Список уникальных курсов:")
        for course in courses:
            print(course)
   
    elif choice == "0":
        print("До свидания!")
        break
        
    else:
        print("Неверный пункт меню")