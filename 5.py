# 5. Write a python script to calculate sum of first N even natural numbers



n=int(input("Enter a number:"))
a=0
for i in range(1,n+1):
    a=a+i
    print("Sum:",a)