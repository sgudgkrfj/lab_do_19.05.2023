#Друге та інші завдання
class School:
    def __init__(self, name, classes, students):
        self.name = name
        self.classes=classes
        self.students = students

    def admit_student(self, student):
        self.students.append(student)


    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name and
                                             s.grade == student.grade, self.students), None)

        if expelled_student is not None:
            self.students.remove(expelled_student)


    def add_class(self,clas):
        self.classes.append(clas)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def promote(self):
        self.grade += 1


    def demote(self):
        self.grade -= 1


    def __str__(self):
        return f"{self.name} - Ранг {self.grade}"

class Class:
    def __init__(self, number,students):
        self.number=number
        self.students=students

    def __iter__(self):
        return iter(self.students)

    def get_average_grade(self, average_grade):
        if len(self.students) == 0:
            return 0
        total_grade = sum(student.grade for student in self.students)
        average_grade = total_grade / len(self.students)
        return average_grade


lisa = Student("Lisa", 15)
nastia = Student("Nastia", 15)
dima = Student("Dima", 16)
gleb = Student("Gleb", 18)
masha = Student("Masha", 16)

class1 = Class(1, [lisa, nastia, dima])
class2 = Class(2, [gleb, masha])

it_step_school = School("ItStep", [class1, class2], [lisa, nastia, dima, gleb, masha])
print(f"Студенти першого класу:")
for students in class1.students:
    print(students)

print(f"Студенти другого класу:")
for students in class2.students:
    print(students)

print("Студенти школи: ")
for students in it_step_school.students:
    print(students)
