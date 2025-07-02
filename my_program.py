n = int(input())
a = n // 100
b = (n % 100) // 10
c = n % 10
xmax = max(a, b, c)
xmin = min(a, b, c)
xavg = (a + b + c) - (xmax + xmin)
if xmax - xmin == xavg:
    print("Число интересное")
else:
    print("Число неинтересное")
