alphabetlist = []
x = int(input("How many words? "))

#number = raw_input("How many words? ")
#type(number)

if x < 2:
    print "You must have more than 1 word!"
    x = int(input("How many words? "))

if x == 2:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)

if x == 3:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)

if x == 4:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)
    toadd = raw_input("4> ")
    alphabetlist.append(toadd)


if x == 5:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)
    toadd = raw_input("4> ")
    alphabetlist.append(toadd)
    toadd = raw_input("5> ")
    alphabetlist.append(toadd)

if x == 6:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)
    toadd = raw_input("4> ")
    alphabetlist.append(toadd)
    toadd = raw_input("5> ")
    alphabetlist.append(toadd)
    toadd = raw_input("6> ")
    alphabetlist.append(toadd)

if x == 7:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)
    toadd = raw_input("4> ")
    alphabetlist.append(toadd)
    toadd = raw_input("5> ")
    alphabetlist.append(toadd)
    toadd = raw_input("6> ")
    alphabetlist.append(toadd)
    toadd = raw_input("7> ")
    alphabetlist.append(toadd)

if x == 8:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)
    toadd = raw_input("4> ")
    alphabetlist.append(toadd)
    toadd = raw_input("5> ")
    alphabetlist.append(toadd)
    toadd = raw_input("6> ")
    alphabetlist.append(toadd)
    toadd = raw_input("7> ")
    alphabetlist.append(toadd)
    toadd = raw_input("8> ")
    alphabetlist.append(toadd)

if x == 9:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)
    toadd = raw_input("4> ")
    alphabetlist.append(toadd)
    toadd = raw_input("5> ")
    alphabetlist.append(toadd)
    toadd = raw_input("6> ")
    alphabetlist.append(toadd)
    toadd = raw_input("7> ")
    alphabetlist.append(toadd)
    toadd = raw_input("8> ")
    alphabetlist.append(toadd)
    toadd = raw_input("9> ")
    alphabetlist.append(toadd)

if x == 10:
    toadd = raw_input("1> ")
    alphabetlist.append(toadd)
    toadd = raw_input("2> ")
    alphabetlist.append(toadd)
    toadd = raw_input("3> ")
    alphabetlist.append(toadd)
    toadd = raw_input("4> ")
    alphabetlist.append(toadd)
    toadd = raw_input("5> ")
    alphabetlist.append(toadd)
    toadd = raw_input("6> ")
    alphabetlist.append(toadd)
    toadd = raw_input("7> ")
    alphabetlist.append(toadd)
    toadd = raw_input("8> ")
    alphabetlist.append(toadd)
    toadd = raw_input("9> ")
    alphabetlist.append(toadd)
    toadd = raw_input("10> ")
    alphabetlist.append(toadd)

if x > 10:
    print "Too many words!"
    x = int(input("How many words? "))

alphabetlist.sort()
print alphabetlist