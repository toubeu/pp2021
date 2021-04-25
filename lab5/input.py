import os
import domains
from domains import Student,Course,Mark,Students,Courses,Marks
import os.path


def check():
    if os.path.isfile("student.dat"):
        with zipfile.ZipFile("student.dat",'r') as zf:
            zf.extractall()
        print (f"extracted premade database\n")
    else:
        print(f"there is no premade database\n")

def addStudent():
    Students =[]
    count= int(input("number of students"))
    for i in range(0,count):
        name= input ("student name:")
        DOB = input ("date of birth:")
        SID = int (input("student ID :"))
        soc=Student(name, DOB, SID)
        Students.append(soc)
        with open("students.txt","r+") as s:
            s.seek(0,os.SEEK_END)
            s.write(f"{name}, {DOB}, {SID}\n")
    return Students


def addCourse():
    count = int(input("number of courses"))
    for i in range(0,count):
        name = input("name")
        CID = int(input("course ID"))
        coc=Course(name, CID)
        Courses.append(coc)
        with open("courses.txt","r+") as c:
            c.seek(0,os.SEEK_END)
            c.write(f"{name}, {CID}\n")
    return Courses


def addMark():
    option = -1
    while (option != "2"):
        print ("do you want to add mark 1 for yes 2 for no")
        option= input("your option  :")
        if (option == "1" ):
            SID = int(input("student ID:"))
            CID = int(input("course ID:"))
            mark= int(input("the mark:"))
            etcs = int (input("etcs"))
            moc=Mark(SID,CID,mark,etcs)
            Marks.append(moc)
            with open("marks.txt", "r+") as m:
                m.seek(0, os.SEEK_END)
                m.write(f"{SID}, {CID},{mark},{etcs}\n")
        if (option !="2") :
            print ("read the sentence again and follow it")
        else: break
    return Marks
def getdata():
    with open("students.txt","r+") as s:
        ls = s.readlines()
        for l in ls:
            if (l):
                data = l.split(",")
                name = data[0]
                DOB = data[1]
                Sid = int(data[2])
                Students.append(Student(name,DOB,SID))
    with open("courses.txt","r+") as c:
        ls = c.readlines()
        for l in ls:
            if (l):
                data = l.split(",")
                name = data[0]
                Cid  = data [1]
                Courses.append(Course(name,Cid))
    with open("marks.txt","r+") as m:
        ls = m.readlines()
        for l in ls:
            if (l):
                data = l.split(",")
                SID = int(data[0])
                SID = int(data[1])
                mark = int(data[2])
                etcs = int(data[3])
                Marks.append(Mark(SID,SID,mark,etcs))







