#  ДЗ 8.2. Паліандром
# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False

from string import punctuation; from copy import deepcopy


def is_palindrome(text: str) -> bool: 
    
    for i in punctuation:
        text = text.replace(i, "")

    text = text.lower().split()
    text = "".join(text)
    text_lst = list(text)
    
    reversed_text = deepcopy(text_lst)
    reversed_text.reverse()

    return text_lst == reversed_text


# print(is_palindrome('A man, a plan, a canal: Panama'))


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")