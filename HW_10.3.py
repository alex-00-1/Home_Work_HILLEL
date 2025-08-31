# ДЗ 10.3. Перевірити чи є парним чи ні


def is_even(digit: int) -> bool:
    """
    Перевірка чи є парним число
    """
    if digit % 2 == 0:
        result = True
    else:
        result = False

    return result


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'

print('OK')
