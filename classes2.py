# numbersListStudents giới hạn số học sinh trong lớp
# listStudents danh sách các học sinh
class Students():
    def __init__(self, numbersListStudents):
        self.numbersListStudents= numbersListStudents
        self.listStudents= []
    def addStudent(self, name):
        if not self.checkLocation():
            return False
        self.listStudents.append(name)
        return True
    #check sớo chỗ còn lại
    def checkLocation(self):
        return self.numbersListStudents - len(self.listStudents)
students=Students(3)
newStudents= ["hoa", "tinh", "khanh", "bao"]

for student in newStudents:
    checkStatus =students.addStudent(student)
    if checkStatus:
        print(f"new students add success is {student}")
    else:
        print(f"no students add: {student}")