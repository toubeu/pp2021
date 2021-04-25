#function for student ( getting info and listing)
def countstudents():
    count = int(input("Student number"))
    return count


def student():
    print("Enter Student Infor : ")
    id = input(" ID : ")
    name = input(" Name : ")
    Birthday = input(" Birthday : ")
    A = {"id": id, "name": name, "birthday": Birthday}
    return A


#creating a list of student
Students = []
count = countstudents()
for i in range(0,count):
    A=student()
    Students += [A]

def students_list(Students):
    for A in Students:
        print(f"id {A['id']},name is {A['name']},birthday is {A['birthday']} ")



#function for course (getting info
def countcourse():
    count = int(input("How many course are there in the semester ?"))
    return count


def course():
    print("Enter Course Infor : ")
    id = input(" ID : ")
    name = input(" Name : ")
    B = {"id": id, "name": name}
    return B


#creating list of courses
Courses =[]
count =countcourse()
for i in range(0,count):
    B=course()
    Courses += [B]


def courses_list(Courses):
    for B in Courses:
        print(f"id {B['id']},name is {B['name']} ")


#function for setting mark
def addmark():
    Sid = input("input student id")
    Cid = input("course id:")
    m = input("mark:")
    C= {"Sid": Sid,"Cid": Cid, "mark": m }
    return C


#create a dict of mark
Marks =[]
count = input("the number of mark you want to input ?")
for i in range(0,int(count)):
    C= addmark()
    Marks += [C]


def printmark():
    for C in Marks:
        print(f"student id is{C['Sid']},course id is {C['Cid']},the mark of course is{C['mark']}")

def selectedprint(Marks,Courses,Students):
    E=input("selected courses")
    for A in Students:
        for B in Courses:
            for C in Marks:
                if E == B['id']:
                    if E == C['Cid']:
                        print(f"the student name is {A['name']}, the mark is {C['mark']}")


