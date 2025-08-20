# ДЗ 7.4. Пошук спільних елементів


def common_elements() -> set:
	division_by_3 = {i for i in range(100) if i % 3 == 0}
	division_by_5 = {i for i in range(100) if i % 5 == 0}
	
	return division_by_3.intersection(division_by_5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print(common_elements())

print("OK")
