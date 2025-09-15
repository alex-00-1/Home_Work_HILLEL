# ДЗ 13.1. Група студентів

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        return f"Info: \n Gender: {self.gender} \n Age: {self.age} \n Name: {self.first_name} Last name: {self.last_name}"



class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book


    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} \n Age: {self.age} \n Record book: {self.record_book}"



class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()


    def add_student(self, student):
        self.group.add(student)


    def delete_student(self, last_name):
        result = self.find_student(last_name)
        
        if result is None:
            return f"The student '{last_name}' is not found"
        else:
            self.group.discard(result)
            return f"The student '{last_name}' was deleted"
        

    def find_student(self, last_name):
        for i in self.group:
            if i.last_name == last_name:
                return i


    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += str(i) + "\n\n"

        return f'Number:{self.number} \n {all_students}'




st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr.group)
# print(gr.find_student('Jobs'))


assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

# print(gr.delete_student('Taylor'))
# print(gr)  # Only one student

# print(gr.delete_student('Taylor'))  # No error!

print("0K")