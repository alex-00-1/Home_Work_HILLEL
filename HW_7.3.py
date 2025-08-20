# ДЗ 7.3. Пошук підрядка

def second_index(text: str, some_str: str) -> int or None: 
    ind = text.find(some_str)
    second_ind = text.find(some_str, ind + 1)

    if second_ind == -1:
        second_ind = None

    return second_ind



assert second_index("sims", "s") == 3, 'Test1' 
assert second_index("find the river", "e") == 12, 'Test2' 
assert second_index("hi", "h") is None, 'Test3' 
assert second_index("Hello, hello", "lo") == 10, 'Test4' 

print('ОК')