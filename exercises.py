import random


# ex1

number = 4
mp = 12 * 12
f = 2.4
word = 'Hello'

# ex2

name2 = 'Tal'
print(f'Number of characters in the name is {len(name2)}')
print(f'The name in uppercase: {name2.upper()}')
print(f'The name in lowercase: {name2.lower()}')
print(f'The first character in the name is {name2[:1]}')
print(f'The character "a" appears {name2.count("a")} time(s) in the name')

# ex3

print('My name is {0}'.format(name2))
print(f'My name is {name2}')

# ex4

num4a = int(input('Please enter the first number: '))
num4b = int(input('Please enter the second number: '))
print(f'{num4a} + {num4b} = {num4a + num4b}')

# ex5

num5 = int(input('Please enter a number: '))
if num5 % 2 == 0:
    print(f'{num5} is an even number')
else:
    print(f'{num5} is an odd number')

# ex6

num6_list = [n for n in range(1, 6)]
num6_list.append(6)
sum6 = 0
for n in num6_list:
    sum6 += n
print(f'The sum is: {sum6}')

# ex7

movie_list7 = ["Fave 1", "Fave 2", "Fave 3", "Fave 4", "Fave 5"]
[print("I Love Avatar") for s in movie_list7 if s == "Avatar"]         # I assure you it's not in there

# ex8

random_list8 = [random.randint(-49, 49) for n in range(10)]
for n in random_list8:
    if n == 0:
        print(f'Number is zero')
    elif n < 0:
        print(f'{n} is a negative number')
    else:
        print(f'{n} is a positive number')

# ex9

word_list9 = []
while True:
    word9 = input("Please enter a word (to end enter 'exit'): ")
    if word9 == 'exit':
        break
    word_list9.append(word9)

print(word_list9)

# ex10

number_list10 = []
sum10 = 0
while True:
    number10 = int(input("Please enter a number (to end enter -1): "))
    if number10 == -1:
        break
    number_list10.append(number10)
    sum10 += number10

print(f'The sum of the numbers is {sum10}')

# ex11

[print(n) for n in range(1, 101)]

# ex12

[print(n) for n in range(0, 51, 3)]

# ex13

list13_1_to_500 = [n for n in range(1, 501)]
print(list13_1_to_500)

# ex14

random14 = random.randint(1, 10)
guess14 = int(input('Please enter a number from 1 to 10 as your guess: '))

if random14 == guess14:
    print('Very good')
else:
    print('Wrong')


# ex15

def double_it(num = 0):
    return num * 2

# ex16

def freq_char(word):
    dict = {}
    for char in word:
        if char in dict:                # checks key
            dict[char] += 1             # adds to value
        else:
            dict[char] = 1              # sets value
    return max(dict, key=dict.get)      # returns key with largest value

word16 = input('Please enter a string: ')
print('The character appearing the most is ' + freq_char(word16))

# ex17

my_set = set()

for n in range(1, 1001):
    my_set.add((random.randint(1, 10)))

print(my_set)

# no number appears more than once


# ex18

my_dict = {
    "book1": 1,
    "book2": 2,
    "book3": 3,
    "book4": 4,
    "book5": 5}

def num_pages(book):
    if my_dict.get(book) == None:
        print("Doesn't exist")
    else:
        print(f'There are {my_dict.get(book)} pages in the "{book}" book')

num_pages('book1')

# ex19

my_tuple = ("first", "second", "third")

# tuples are immutable, so its values cannot be changed.


# other exercises, see separately
