from random import randint

first = randint(1, 10)
second = randint(1, 10)
third = randint(1, 10)
print('First =', first)
print('Second =', second)
print('Third =', third)
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)