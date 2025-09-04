# ДЗ 11.3. Перевірка на парність.


def is_even(number: int) -> bool:
    """
    Check if the number is even without division

    Args:
        number: the integer we need to check

    Returns:
        bool: True if the number is even, else False
    """

    return str(number)[-1] in "02468"


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'


print("OK")
