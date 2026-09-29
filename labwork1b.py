students = {}
courses = {}
marks = {}


def input_student():
    n = int(input("enter number of student: "))

    for i in range(n):
        id = int(input("enter student ID: "))
        name = input("enter student name: ")
        Dob = input("enter DoB: ")

        students[id] = {
            "student name": name,
            "date of birth": Dob
        }

    print(students)


def input_course():
    k = int(input("enter number of courses: "))

    for i in range(k):
        idcourse = input("enter course ID: ")
        name_c = input("enter course name: ")

        courses[idcourse] = {
            "name course": name_c
        }

    print(courses)


def input_mark():

    print(courses)

    course_id = input("enter id course: ")

    if course_id not in courses :
        print("invalid")
        return 
    else:
        marks[course_id] = {}

        for student in students.keys():
            k = float(input("enter your mark : "))
            marks[course_id][student] = k
    print(".................")
    print(marks)

input_student()
input_course()
input_mark()