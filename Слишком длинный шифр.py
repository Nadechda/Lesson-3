n = int(input('Введи число от 3 до 20: '))
num1 = list(range(1, n))
num2 = list(range(1, n))
result = ''

for i in num1:
    for j in num2:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            if n % (pn1 + pn2) == 0:
                result = result + str(pn1) + str(pn2)
print('Пароль', result)
