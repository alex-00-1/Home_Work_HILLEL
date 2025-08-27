# ДЗ 9.1. Визначити популярність певних слів у тексті


def popular_words (text: str, words: list) -> dict: 
    
    count_lst = []
    
    for i in words:
        i += " "
        count_lst.append(text.lower().count(i))

    dct = dict(zip(words, count_lst))
    

    return dct


# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'

print('OK')
