# ДЗ 7.1. Вітання

def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {} and I'm {} years old".format(name, age)


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

# print(say_hi("Vlad", 88))