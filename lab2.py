class Student:
    def __init__(self, name, DoB, Sid):
        self.name = name
        self.DoB = DoB
        self.Sid = Sid

    def __str__(self):
        return f"the student with an id {self.Sid} name is {self.name},the date of birth is {self.DoB}"

    def getID(self):
        return self.Sid


class Course:
    def __init__(self, name, Cid):
        self.name = name
        self.Cid = Cid

    def __str__(self):
        return f"the course with an id {self.Cid} name is {self.name}"

    def getCID(self):
        return self.Cid


class Mark:
    def __init__(self, Sid, Cid, mark):
        self.Sid = Sid
        self.Cid = Cid
        self.mark = mark


    def __str__(self):
        return f"student got id{self.Sid} got {self.mark} in course {self.Cid}"

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
            moc=Mark(SID,CID,mark)
            Marks.append(moc)
        if (option !="2") :
            print ("read the sentence again and follow it")
        else: break
    return Marks
def students_list(Students):
    for Student in Students:
        print(Student)

def courses_list(Courses):
    for Course in Courses:
        print(Course)

def selectedmark_list(Students,Courses,Marks):
    E = input("selected courses")
    for Mark in Marks:
        if (Mark.Cid == int(E)):
            for Student in Students:
                if (Mark.Sid == Student.Sid):
                    for Course in Courses:
                        if (Course.Cid == int(E)):
                            print(f"student {Student.name} have {Mark.mark} in course  {Course.name1}")
def main():
    Students =addStudent()
    Courses =addCourse()
    Marks=addMark()
    students_list(Students)
    courses_list(Courses)
    selectedmark_list(Students,Courses,Marks)
if __name__ == "__main__":
    main()
