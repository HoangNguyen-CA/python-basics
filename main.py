person = {
    'firstname': 'Joe',
    'lastname': 'Mama'
}

# formatted string
print(f'wow {person}')
print(person.items())
print(len(person))

'''
FUNCTIONS
'''


def say_hello(name):
    print(name)


def get_sum(num1, num2):
    temp_sum = num1 + num2
    return temp_sum


print(get_sum(1, 5))

'''
CONDITIONALS
'''

bigger = 100
smaller = -100

if bigger > smaller:
    print(f'{bigger} is bigger than {smaller}')

if bigger > smaller and True:
    print('TRUE')

if bigger > smaller or True:
    print('Always True')
'''
MEMBERSHIP OPERATORS
'''

numbers = [1, 2, 3, 4, 5, 6]

if 1 in numbers:
    print('1')
if 1 not in numbers:
    print('not 1')

'''
LOOPS
'''
