import pickle

import os

ch = 'y'

fle = open("Test.txt", "wb+")

fl2 = open("Temp.txt", "ab+")

while ch == 'y' or ch == 'Y':

    L = []

    rollno = int(input("Enter roll no.: "))

    L.append(rollno)

    name = input("Enter your name: ")

    L.append(name)

    pickle.dump(L,fle)

    ch = input("Do you want to add more?(Y or N): ")

print()

print("You have entered the following records:")



fle.seek(0)

while 1:

    try:

        b = pickle.load(fle)

        print(b)

    except:

        break



n = int(input("Enter roll number to be searched: "))

fle.seek(0)

x = fle.tell()

flag = 0

while 1:

    try:

        b = pickle.load(fle)

        if b[0] == n:

            print("Record found, details are:")

            print(b)

            flag += 1

    except:

        break

if flag == 0:

    print("Record not found.")



fle.seek(0)

flag = 0

n = int(input("Enter roll number to be modified: "))

while 1:

    try:

        b = pickle.load(fle)

        if b[0] == n:

            print("Record found")

            pos = fle.tell()

            print(pos)

            newpos = pos - x

            print(newpos)

            fle.seek(newpos)

            L = []

            rollno = int(input("Enter roll no: "))

            L.append(rollno)

            name = input("Enter name: ")

            L.append(name)

            pickle.dump(L, fl2)

            flag += 1

        else:

            pickle.dump(b, fl2)

    except:

        break



if flag == 0:

    print("Record not found")

    fle.close()

    fl2.close()

else:

    fle.close()

    fl2.close()

    os.remove("Test.txt")

    os.rename("Temp.txt", "Test.txt")

    fle = open("Test.txt", "rb")

    print("New contents of the file are: ")

    fle.seek(0)

    while 1:

        try:

            c = pickle.load(fle)

            print(c)

        except:

            break



fle.close()
