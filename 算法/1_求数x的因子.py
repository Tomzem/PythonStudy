number = int(input(""))
divisors = ()
for i in range(1, number):
    if number % i == 0:
        divisors = divisors + (i, )
print(divisors)