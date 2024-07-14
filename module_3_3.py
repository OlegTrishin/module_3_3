def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()              # Без аргументов
print_params(a=5)           # С аргументом a=5
print_params(b=25)          # С аргументом b=25
print_params(c=[1, 2, 3])   # С аргументом c=[1,2,3]

# Распаковка параметров
values_list = [10, 'первая строка', False]
values_dict = {'a': 7, 'b': 'вторая строка', 'c': True}

print_params(*values_list)      # Передаём values_list в функцию print_params
print_params(**values_dict)     # Передаём values_dict в функцию print_params

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
