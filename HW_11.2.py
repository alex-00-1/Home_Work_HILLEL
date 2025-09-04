# ДЗ 11.2. Заповнення списку кубами чисел


def generate_cube_numbers(end: int):
    """
    Generator of cube numbers

    Args:
        end: the last number in range

    Returns:
        the cube of number which less the argument in variable "end"
    """
    
    for i in range(2, end + 1):

        cube = i ** 3

        if cube > end:
            return None
        else:
            yield cube



# print(list(generate_cube_numbers(100)))

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print("OK")