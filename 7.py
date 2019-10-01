#Q7 To check whether a given number is fibonacci number or not

num=int(input("Enter a number to check:"))

a,b=0,1
c=0
if(num==a or num==b):
    print("Number present in Fibonacci Series")
    
while(c<=num):
    c=a+b
    if(c==num):
        print("Number present in Fibonacci Series")
        break
    a=b
    b=c


