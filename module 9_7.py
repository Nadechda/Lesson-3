def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        f=True
        if n <= 1:
            f = False
        if n == 2:
            f = True
        if n % 2 == 0:
            f = False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                f = False
        if f:
            print('Простое')
        else:
            print('Составное')

        return n

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(3, 3, 3)
print(result)
