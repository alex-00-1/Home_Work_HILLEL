# ДЗ 10.2. Знайти перше слово

import string

def first_word(text: str) -> str:
    """
    Пошук першого слова
    """

    for i in string.punctuation:
        if i == "'":
            continue

        text = text.replace(i, " ")

    first_word = text.split()
    # print(first_word[0])

    return first_word[0]
  

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')