template = ['5', 'x', 'x', '#', '#', '#']

print(template)

combs = []

combs.pop(2)
combs.pop(2)
combs.pop(1)

toadd = input("Username> ")

numbs1 = toadd[5]
numbs2 = toadd[6]
numbs3 = toadd[7]

digit3 = (int(toadd[7]) - 2)

combs.append(numbs1)
combs.append(numbs2)
combs.append(numbs3)

combs.insert(1, numbs2)
combs.insert(2, digit3)

print(combs)
