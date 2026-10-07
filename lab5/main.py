import math
import numpy as np
import os
import zipfile
from domains.student import Student
from domains.course import Course

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
            self.students.append(s)# prac5

         
        if len(self.students) > 0:     
            with open("students.txt", "w") as f:     
                for student_item in self.students:        
                    st_id = student_item.get_id()
                    st_name = student_item.get_name()
                    st_dob = student_item.get_dob()
                    f.write(f"{st_id},{st_name},{st_dob}\n")  
                        


    def input_course(self):
        n = int(input("Enter number of courses: "))
        a = int(input("Enter number of credits: "))
        for i in range(n):
            idc = input("Enter course ID: ")
            namec = input("Enter course name: ")
            c = Course(namec,idc,a)
            self.courses.append(c)

         
        if len(self.courses) > 0:     
            with open("courses.txt", "w") as f:     
                for course_item in self.courses:                    
                    cr_id   = course_item.get_id()
                    cr_name = course_item.get_name()
                    cr_credits = course_item.get_credits()
                    f.write(f"{cr_id},{cr_name},\n")
                     

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

        if len(self.marks) > 0:
            with open("marks.txt", "w") as f:
                 
                for c_id, student_marks_dict in self.marks.items():
                    
                    for st_id, mark_value in student_marks_dict.items():
                        
                        f.write(f"{c_id},{st_id},{mark_value}\n")

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

    def compress_data():
        with zipfile.ZipFile("students.dat","w") as zipf:
            if os.path.exists("students.txt"):
                zipf.write("students.txt")
            if os.path.exists("courses.txt"):
                zipf.write("courses.txt")
            if os.path.exists("marks.txt"):
                zipf.write("marks.txt")

    def load_data(self):
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as zipf:
                zipf.extractall(".")

            if os.path.exists("students.txt"):
                with open("students.txt", "r") as f:
                    for line in f:
                        st_id, st_name, st_dob = line.strip().split(',')
                        self.students.append(Student(st_id, st_name, st_dob))

            if os.path.exists("courses.txt"):
                with open("courses.txt", "r") as f:
                    for line in f:
                        cr_id, cr_name, cr_credits = line.strip().split(',')
                        self.courses.append(Course(cr_name, cr_id, int(cr_credits)))

            if os.path.exists("marks.txt"):
                with open("marks.txt", "r") as f:
                    for line in f:
                        c_id, st_id, mark_value = line.strip().split(',')
                         
                        if c_id not in self.marks:
                            self.marks[c_id] = {}
                        self.marks[c_id][st_id] = float(mark_value)

if __name__ == "__main__":
    system = System()
    system.input_student()
    system.input_course()
    system.input_mark()
    system.gpa() 
    system.compress_data()                