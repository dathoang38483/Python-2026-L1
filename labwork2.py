class Student :
    def __init__(self,id,name,Dob):
        self.__name = name
        self.__id  = id
        self.__Dob = Dob
    def get_Id(self):
        return self.__id
    def get_Name(self):
        return self.__name
    def get_dob(self):
        return self.__Dob
    def list_info(self):
        print("ID: ",self.__id)
        print("Name: ",self.__name)
        print("Date of Birth: ",self.__Dob)
        

class Course:
    def __init__(self,nameC,Idc):
        self.__nameCourse = nameC
        self.__id_courese = Idc
    def get_IDC(self):
        return self.__id_courese
    def get_NameC(self):
        return self.__nameCourse
    def list_info(self):
        print("Course Name: ",self.__nameCourse)
        print("Course ID: ",self.__id_courese)

class System:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        self.input_student()
        self.input_course()
        self.input_mark()
    def input_student(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            s = Student(id,name,dob)
            self.students.append(s)
    def input_course(self):
        n = int(input("Enter number of courses: "))
        for i in range(n):
            idc = input("Enter course ID: ")
            namec = input("Enter course name: ")
            c = Course(namec,idc)
            self.courses.append(c)
    def input_mark(self):
        course_id = input("enter id course: ")
        if course_id not in [c.get_IDC() for c in self.courses]:
            print("Invalid course ID")
            return
        self.marks[course_id] = {}
        for student in self.students:
            print(f"enter mark for student {student.get_Name()} (ID: {student.get_Id()}): ")
            k = float(input("enter your mark: "))
            self.marks[course_id][student.get_Id()] = k


my_school = System()

