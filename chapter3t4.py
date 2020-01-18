lst = input('Введите числа через пробел: ').split(' ')
lst = list(map(int, lst))
m = max(lst)
m =int(m)
if m < 0:
    print(1)

else:
    for n in range(1,m + 2):
        if n not in lst:
            print(n)
            break


        