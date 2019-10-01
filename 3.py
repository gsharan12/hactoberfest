#3. WAP to sort a list of numbers

a=[]
n=int(input("Enter value of n:"))
for i in range(0,n):
    num=int(input("Enter a number"))
    a.append(num)

#sorting
for i in range(0,n):
    for j in range(0,n-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]


print(a)
    
