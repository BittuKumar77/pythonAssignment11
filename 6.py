# 6. Write a python script to calculate factorial of a given number



n=int(input("Enter a number:"))
a=1
for i in range(1,n+1):
    a=a*i
    print("factorial of ",n,"is",a)