num = int(input())
last_digit = num % 10
first_digit = num // 10
slf_d = first_digit + last_digit
print("Число десятков -", first_digit)
print("Число единиц -", last_digit)
print("Сумма первого и последнего числа =", slf_d)
