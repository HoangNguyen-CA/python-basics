person = {
    'firstname': 'Joe',
    'lastname': 'Mama'
}

# formatted string
print(f'person: {person}')
print(person.items())
print(len(person))

# floor division, normal division ALWAYS returns a float.
print(12 // 5)

# raw strings don't get escaped by "\" character
print(r'new\n line')

# triple quotes can be used for multi-line strings
print('''multiline
string''')

# arrays/strings can be indexed with negative numbers to return last elements
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"last element: {arr[-1]}")

# arrays can also be sliced, first index is included, second index is excluded, slice returns a shallow copy of a list!
print(f'slice 3-7: {arr[3:7]}, slice 3-none: {arr[3:]} slice none-3: {arr[:3]}')

# python strings are immutable, to change one, a new string must be created, arrays are mutable.

# use .append() to add items to end of array
arr.append(11)
print(arr)

# you can re-assign array slices
arr[1:9] = [0]
print(arr)

# multiple assignment

a, b = 1, 2

'''
FUNCTIONS
'''

# strings can be repeated with '*' and concatenated with '+'
print(5 * 'helloworld ')


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
