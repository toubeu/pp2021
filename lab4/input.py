import domains
from domains import Student,Course,Mark

def addStudent():
    Students =[]
    count= int(input("number of students"))
    for i in range(0,count):
        name= input ("student name:")
        DOB = input ("date of birth:")
        SID = int (input("student ID :"))
        soc=Student(name, DOB, SID)
        Students.append(soc)
    return Students


def addCourse():
    Courses =[]
    count = int(input("number of courses"))
    for i in range(0,count):
        name = input("name")
        CID = int(input("course ID"))
        coc=Course(name, CID)
        Courses.append(coc)
    return Courses


def addMark():
    Marks=[]
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
        if (option !="2") :
            print ("read the sentence again and follow it")
        else: break
    return Marks