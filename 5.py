#Q5 search number in a list

a=[]
n=int(input("Enter value of n:"))
for i in range(0,n):
    num=int(input("Enter a number"))
    a.append(num)

ctr=0
sch=int(input("Enter a number to search"))
for i in range(0,n):
    if(a[i]==sch):
        ctr=ctr+1

if(ctr>0):
    print("Number present in list")
else:
    print("Number not present in list")
    
