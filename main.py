import numpy as np

# 1. Створення масиву з 200 випадкових чисел від -100 до 100
arr = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(arr)

# 2. Маска для додатних чисел
positive_mask = arr > 0
positive_numbers = arr[positive_mask]

print("\nДодатні числа:")
print(positive_numbers)

# 3. Замінюємо всі від’ємні значення на 0
modified_arr = arr.copy()
modified_arr[modified_arr < 0] = 0

print("\nМасив після заміни від’ємних значень на 0:")
print(modified_arr)

# 4. Обчислення середнього значення
average = np.mean(modified_arr)

print("\nСереднє значення масиву:")
print(average)