# ДЗ 9.2. Різниця між числами

import math

def difference(*args) -> int:
    """
    Finds the difference beetwen max and min numbers

    Args:
        args: gets numbers

    Returns:
        integer or float
    """
    if args:
        max_num = max(args)
        min_num = min(args)

        result = round(max_num - min_num, 1)
    else:
        result = 0

    return result


# print(difference(difference(10.2, -2.2, 0, 1.1, 0.5)))
# print(difference(difference(1, 2, 3)))

assert difference(1, 2, 3) == 2, 'Test1' 
assert difference(5, -5) == 10, 'Test2' 
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3' 
assert difference() == 0, 'Test4' 

print('OK')
