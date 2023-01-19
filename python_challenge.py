"""--Assignement--
Create and call a python function that :
- stores a random integer A between 1 and 9
- stores a random integer B between 1 and 9
- multiplies A and B together as C
- Prints A and C for every result until C = 4
- If C = 4 , print ‘Success!’ and the results for A and B
- Store your code on a GitHub account and share it with the email-address given in the SQL test, including your CV"""

from random import randint


def challenge():
    while True:
        a = randint(1, 9)
        b = randint(1, 9)
        c = a * b
        print(f'{a = } and {c = }')
        if c == 4:
            print(f'Success! {a = } {b = }')
            break


challenge()
