# Code to count the No. of vowels in a Text file
file = open("textfile.txt","r")
line =file.read()
c=0
for i in line:
    word=i.split(" ")
    if i=="A" or i=="a" or i=="E" or i=="e" or i=="I" or i=="i"or i=="O"or i=="o"or i=="U"or i=="u":
        c+=1
print ("count of vowels is ",c)
file.close()

