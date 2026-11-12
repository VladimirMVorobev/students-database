from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    faculty = Column(String, nullable=False)
    course = Column(String, nullable=False)
    grade = Column(Integer, nullable=False)


engine = create_engine("sqlite:///students.db")

Base.metadata.create_all(engine)