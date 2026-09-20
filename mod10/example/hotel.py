from dog import Dog

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)

    def dog_checkout(self, dog):
        self.dogs.remove(dog)

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

dog1=Dog("Buddy", 10)
dog2=Dog("Max", 5, "arf arf")
hotel = Hotel()
hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()
hotel.dog_checkout(dog1)
hotel.greet_dogs()


""" in class exercises
school has students
scl has course (Python 1)
course has course instance (TXLS26-B)
teacher can add a student to a course instance
teacxher can give a grade to a student 
teacher view all greades of their instances
or the grade of a student in a course instance"""

class Student:

  def __init__(self, student_id, name):
    self.student_id = student_id
    self.name = name


class Teacher:

  def __init__(self, teacher_id, name):
    self.teacher_id = teacher_id
    self.name = name

  # Teacher adds a student to a course instance
  def enroll_student(self, student, instance):
    instance.add_student(student)
    print(f"{self.name} enrolled {student.name} into {instance.instance_code}.")

  # Teacher assigns a grade to a student in a course instance
  def assign_grade(self, student, instance, grade):
    instance.set_grade(student, grade)
    print(
        f"{self.name} graded {student.name}: {grade} in"
        f" {instance.instance_code}."
    )

  # Teacher views all grades in a course instance they teach
  def view_instance_grades(self, instance):
    print(f"\n--- Grades for {instance.instance_code} ---")
    for student, grade in instance.grades.items():
      grade_display = grade if grade is not None else "Not Graded"
      print(f"Student: {student.name} | Grade: {grade_display}")

  # Teacher views a specific student's grade in a course instance
  def view_student_grade(self, student, instance):
    grade = instance.grades.get(student, "Not enrolled")
    print(f"{student.name}'s grade in {instance.instance_code}: {grade}")


class Course:

  def __init__(self, course_code, name):
    self.course_code = course_code
    self.name = name


class CourseInstance:

  def __init__(self, instance_code, course, teacher):
    self.instance_code = instance_code
    self.course = course  # Association with Course
    self.teacher = teacher  # Association with Teacher
    self.students = []  # List of enrolled Student objects
    self.grades = {}  # Map: Student object -> Grade (int/str)

  def add_student(self, student):
    if student not in self.students:
      self.students.append(student)
      self.grades[student] = None

  def set_grade(self, student, grade):
    if student in self.students:
      self.grades[student] = grade
    else:
      print(f"Error: {student.name} is not in this instance.")


class School:

  def __init__(self, name):
    self.name = name
    self.students = []
    self.courses = []
    self.instances = []


