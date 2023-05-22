#Друге та інші завдання
class School:
    def __init__(self, name, classes, students):
        self.name = name
        self.classes=classes
        self.students = students

    def admit_student(self, student):
        self.students.append(student)
        print(f"{student.name} був допущений до {self.name}")

    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name and
                                             s.grade == student.grade, self.students), None)

        if expelled_student is not None:
            self.students.remove(expelled_student)
            print(f'{expelled_student.name} був виключений з {self.name}')
        else:
            print(f'{student.name} не знайдено в {self.name}')
    def add_class(self,clas):
        self.classes.append(clas)
        print(f"{clas} був доданий до {self.classes}")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def promote(self):
        self.grade += 1
        print(f"{self.name} був підвищений до рангу {self.grade}")

    def demote(self):
        self.grade -= 1
        print(f"{self.name} був понижений до рангу {self.grade}")

    def __str__(self):
        return f"{self.name} - Ранг {self.grade}"

class Classs:
    def __init__(self, number,students):
        self.number=number
        self.students=students
        print(f"Номер класу: {self.number}, Студенти: {self.students}")

    def __iter__(self):
        return iter(self.students)

lisa=Student("Lisa", 15)
nastia=Student("Nastia", 15)
dima=Student("Dima", 16)
gleb=Student("Gleb", 18)
masha=Student("Masha", 16)
my_class=School("ItStep", Classs(1, [lisa, nastia, dima, gleb, masha]), [lisa, nastia, dima, gleb, masha])

for student in my_class.classes:
    print(student)





