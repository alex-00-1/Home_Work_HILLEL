# ДЗ 14.1. Виняток користувача

class MyException(Exception):
    pass



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
        if len(self.group) == 10:
            raise MyException("The max studen's num is 10")
        else:
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
st3 = Student('Male', 25, 'Vlad', 'Test1', 'AN145')
st4 = Student('Male', 25, 'Max', 'Test2', 'AN145')
st5 = Student('Male', 25, 'David', 'Test3', 'AN145')
st6 = Student('Male', 27, 'Alex', 'Test4', 'AN145')
st7 = Student('Female', 29, '', 'Test5', 'AN145')
st8 = Student('Female', 22, 'Liza', 'Test6', 'AN145')
st9 = Student('Female', 21, 'Liza', 'Test7', 'AN145')
st10 = Student('Female', 20, 'Liza', 'Test8', 'AN145')
st11 = Student('Male', 30, 'Ivan', 'Bondar', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

gr.add_student(st11)


# print(gr.find_student("Bondar"))
# print(gr)
