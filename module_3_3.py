#Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params(1,2,3)
print_params(1,2)
print_params()

#Распаковка параметров
values_list=[1,'Hello',2.5]
values_dict={'a': 2, 'b' :'World','c': 3.5}
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)