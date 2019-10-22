#!/usr/bin/env python3

# this is the first comment
spam = 1  # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(text)

print(2 + 2)

s = 'supercalifragilisticexpialidocious'
print(s)
length = len(s)
print("Length:", length)

squares = [1, 4, 9, 16, 25]
print(squares)

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4 ** 3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
num = len(letters)
print(num)

letters = ['a', 'b', 'c']
n = [1, 2, 3]
x = [letters, n]
print(x)

print(x[0])

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 1000:
    print(b)
    a, b = b, a + b

i = 256 * 256
print('The value of i is', i)

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b

# x = int(input("Please enter an integer: "))
x = 1

if x < 0:
    x = 0
    print('Negative changed to zero')
    print('Zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Measure some strings (Count Letters):
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print(words)

# for i in range(10000000):
#    print(i)

r = list(range(16))
print(r)

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Now call the function we just defined:

fib(2000)
