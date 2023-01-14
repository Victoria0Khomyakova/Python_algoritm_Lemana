import random

while True:
    n = int(input('Введите тестируемое число: '))
    if n == 0 or n == 1:
        break
    simple = True
    col = 0

    if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0) and (n != 2 and n != 3 and n != 5):
        simple = False
    else:
        for i in range(10):
            a = random.randint(1, n-1)
            k=1
            for j in range((n - 1) // 2):
                k *=a
                k %= n
            if k == 1 or k == (n - 1):
                col += 1
            else:
                simple = False
                break

    if simple:
        print(f'Число {n} простое')
    else:
        print(f'Число {n} составное')

