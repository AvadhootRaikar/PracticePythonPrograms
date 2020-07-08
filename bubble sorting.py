List=eval(input("Enter a list to be sorted :"))
print("Entered list is :", List)
num=len(List)
for i in range(num):
    for j in range (0,num-i-1):
        if List[j]>List[j+1]:
            List[j],List[j+1]=List[j+1],List[j]
print("List after sorting :",List)
