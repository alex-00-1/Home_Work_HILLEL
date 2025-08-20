# ДЗ 7.2. Модифікувати рядок



def correct_sentence(text: str) -> str:

    if "." not in text[-1]:
        add_dot = list(text)
        add_dot.append(".")
        str_with_dot = "".join(add_dot)
    else:
        str_with_dot = text

    lst = str_with_dot.split()
    lst[0] = lst[0].capitalize()
    final_result = " ".join(lst)

    return "{}".format(final_result)


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')