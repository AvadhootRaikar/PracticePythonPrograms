# Code to count the no. of words in a text file
file = open("textfile.txt","r")
line =file.read()
c=0
for i in line:
    word=i.split(" ")
    c+=1
print ("Number of words are ",c)
file.close()

