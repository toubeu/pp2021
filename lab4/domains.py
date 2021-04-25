class Student:
    gpa =0.0
    def __init__(self, name, DoB, Sid):
        self.name = name
        self.DoB = DoB
        self.Sid = Sid

    def __str__(self):
        return f"the student with an id {self.Sid} name is {self.name},the date of birth is {self.DoB}"

    def getID(self):
        return self.Sid


class Course:
    def __init__(self, name, Cid,):
        self.name = name
        self.Cid = Cid
    def __str__(self):
        return f"the course with an id {self.Cid} name is {self.name}"

    def getCID(self):
        return self.Cid


class Mark:
    def __init__(self, Sid, Cid, mark,etcs):
        self.Sid = Sid
        self.Cid = Cid
        self.mark =mark
        self.etcs = etcs

    def __str__(self):
        return f"student got id{self.Sid} got {self.mark} in course {self.Cid}"