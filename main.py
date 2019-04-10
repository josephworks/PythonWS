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
4 ** 3  # the cube of 4 is 64, not 65!
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

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 1000:
    print(b)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
