#программа проверяет введено ли трехзначное число и если да, то выводит на экран сумму его чисел

num = int(input("Введите трехзначное число: "))

if num < 100 or num > 999:
    print("Вы ввели неправильное число!")
else:
    digit1 = num // 100
    digit2 = (num // 10) % 10
    digit3 = num % 10
    sum_digits = digit1 + digit2 + digit3
    print("Сумма цифр трехзначного числа ", num, " равна ", sum_digits)