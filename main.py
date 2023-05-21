class School:
    def __init__(self, name, techers):
        self.name=name
        self.teachers=techers
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
        print(f"{teacher.name} був допущений до навчання")
class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject=subject
        self.classes=classes
    def __str__(self):
        return f"Ім'я: {self.name}, предмет: {self.subject}," \
               f" класи, в яких викладає: {self.classes}"

my_school=School("Моя школа",[Teacher("Тетяна Анатоліївна", "Математика", [1,2,3,4,5]), Teacher("Валентина Володимирівна", "Історія", [4,5,6,7,8,9])])
print("Початкові вчителі:")
for teacher in my_school.teachers:
    print(teacher)
my_school.add_teacher(Teacher("Наталія Миколаївна", "Фізика", [7,8,9,10,11]))
print("Оновлення")
for teacher in my_school.teachers:
    print(teacher)