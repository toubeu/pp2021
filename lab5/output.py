import numpy as np
import math
import domains
from domains import Student,Course,Mark

def students_list(Students):
    for Student in Students:
        print(Student)


def courses_list(Courses):
    for Course in Courses:
        print(Course)


def selected_mark(Students,Courses,Marks):
    E = input("selected courses")
    for Mark in Marks:
        if (Mark.Cid == int(E)):
            for Student in Students:
                if (Mark.Sid == Student.Sid):
                    for Course in Courses:
                        if (Course.Cid == int(E)):
                            print(f"student {Student.name} have {Mark.mark} in course  {Course.name}")
def calGPA(Marks,Students):
    for Student in Students:
        ETCcount=0
        for Mark in Marks:
            if (Student.Sid == Mark.Sid):
                m=[]
                etc=[]
                m= np.append(m,[Mark.mark],axis=0)
                etc= np.append(etc,[Mark.etcs],axis=0)
                ETCcount= ETCcount + Mark.etcs
        GPA= (m@etc)/ETCcount
        Student.gpa= GPA

def sortGPA(Students):
    GPA_list = sorted(Students, key=lambda x: x.gpa, reverse=True)
    print(f"sorted gpa list:")
    for Student in GPA_list:
        print(f"\n {Student.name}")

def compressing():
    with zipfile.ZipFile("student.dat","w") as myzip:
        myzip.write("students.txt")
        myzip.write("courses.txt")
        myzip.write("marks.txt")
