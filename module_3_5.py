def get_multiplied_digits(number):
    if number==0:
        return 1
    else:
        return number % 10 * get_multiplied_digits(number // 10)

#n = int(input('Введи число: '))
#print('Произведение цифр: ', get_multiplied_digits(n))
result = get_multiplied_digits(40203)
print(result)