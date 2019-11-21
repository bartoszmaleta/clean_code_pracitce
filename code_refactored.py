import math
import random

a = []
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))


def return_list_with_10_random_numbers():
    for i in range(10):
        a.append(random.randint(1, 99))
    return a


list_with_10_numbers = return_list_with_10_random_numbers()

for i in range(1):
    g = int(input("Enter an integer from 1 to 99: "))
    while list_with_10_numbers[i] != g:
        if g < a[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > list_with_10_numbers[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

b = []
b.append(random.randint(1, 49)) 
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")