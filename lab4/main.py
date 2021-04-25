import math
import numpy as np
import domains
from domains import Student,Course,Mark
import input as inp
import output as out


def main():
    Students =inp.addStudent()
    Courses = inp.addCourse()
    Marks=inp.addMark()
    out.students_list(Students)
    out.courses_list(Courses)
    out.calGPA(Marks,Students)
    out.sortGPA(Students)
if __name__ == "__main__":
    main()