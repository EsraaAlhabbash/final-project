System
# TODO 1 Enter your name and submission date
Name : Esraa alhabbash
Delivery Date :21-6-2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
solution
import uuid


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    # TODO 3 define static variable indicates total student count
solution

class Student:
    total_students = 0

    
    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self):
        pass
solution
def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1




    # TODO 5 define a method to enroll new course to student courses list

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__
solution
def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict_




    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        pass
solution

def get_student_courses(self):
        for course in self.courses_list:
            print("Course Name:", course.course_name, " - Course Mark:", course.course_mark)









    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        pass
solution

def get_student_average(self):
        if len(self.courses_list) == 0:
            print("No Courses Found!")
            return 0
        total = 0
        for course in self.courses_list:
            total += course.course_mark
        return total / len(self.courses_list)









# in Global Scope
# TODO 8 declare empty students list

solution

students_list = []













while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))
solution 
while True:
    try:
        selection = int(input("1.Add New Student\"
                              "2.Delete Student\"
                              "3.Display Student\"
                              "4.Get Student Average\"
                              "5.Add Course to student with mark.\"
                              "6.Exit"))
    except ValueError:
        print("Invalid Selection!")
        continue

  









    if selection == 1:

        # TODO 10 make sure that Student number is not exists before
        student_number = input("Enter Student Number")

        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

solution
if selection == 1:
        student_number = input("Enter Student Number: ")
        is_duplicate = False
        for student in students_list:
            if student.student_number == student_number:
                is_duplicate = True
                break
        if is_duplicate:
            print("Student Number already exists!")
        else:
            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value!")





        # TODO 11 create student object and append it to students list

        print("Student Added Successfully")

solution
student = Student(student_name, student_age, student_number)
            students_list.append(student)
            print("Student Added Successfully!")




    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

solution
elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                students_list.remove(student)
                print("Student Deleted Successfully!")
        else:
            print("Student Not Exist!")





    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
 solution

elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                student_details = student.get_student_details()
                print("Student Details:")
                for key, value in student_details.items():
                    if key == "courses_list":
                        continue
                    print(key.capitalize(), ":", value)
                student.get_student_courses()
                break
        else:
            print("Student Not Exist!")



    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

solution

elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                student_average = student.get_student_average()
                print("Student Average:", student_average)
                break
        else:
            print("Student Not Exist!")







    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses

solution
elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                while True:
                    try:
                        course_mark = int(input("Enter Course Mark: "))
                        break
                    except ValueError:
                        print("Invalid Value!")
                student.enroll_course(course_name, course_mark)
                print("Course Enrolled Successfully!")
                break
        else:
            print("Student Not Exist!")













    else:
    
        # TODO 16 call a function to exit the program
        pass


else:
        exit()








