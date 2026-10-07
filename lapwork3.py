import math
import numpy as np
class Student :
    def __init__(self,id,name,Dob):
        self.__name = name
        self.__id  = id
        self.__Dob = Dob
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__Dob
    def list_info(self):
        print("ID: ",self.__id)
        print("Name: ",self.__name)
        print("Date of Birth: ",self.__Dob)
        

class Course:
    def __init__(self,name,id,credits):
        self.__name = name
        self.__id = id
        self.__credits = credits
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def list_info(self):
        print("Course Name: ",self.__name)
        print("Course ID: ",self.__id)

class System:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
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
        a = int(input("Enter number of credits: "))
        for i in range(n):
            idc = input("Enter course ID: ")
            namec = input("Enter course name: ")
            c = Course(namec,idc,a)
            self.courses.append(c)
    def input_mark(self):
        course_id = input("enter id course: ")
        if course_id not in [c.get_id() for c in self.courses]: #  :self.courses have name course and id , but we need onely id so  use c.get_id() it take on ly the id course,  
            print("Invalid course ID")
            return
        self.marks[course_id] = {} # step1 create a chest for each course
        for student in self.students:
            print(f"enter mark for student {student.get_name()} (ID: {student.get_id()}): ")
            k = float(input("enter your mark: "))
            k = math.floor(k *10 )/10
            self.marks[course_id][student.get_id()] = k # step 2 " self.marks[course_id]" open chest ,"[student.get_id()]" find student id in chest, " = k" put mark in chest
    def gpa(self):
        for student in self.students:
            list_marks = []
            list_credits = []
            for course_id, mark in self.marks.items():
                if student.get_id() in mark:
                    list_marks.append(mark[student.get_id()])
                    for course in self.courses:
                        if course.get_id() == course_id:
                            list_credits.append(course.get_credits())
            if list_marks and list_credits:# in python list empty list is false, if A and B that means A have somthing and B alse have soting pass to next step
                gpa = np.average(list_marks, weights=list_credits)
                print(f"GPA for student {student.get_name()} (ID: {student.get_id()}): {gpa:.2f}")




