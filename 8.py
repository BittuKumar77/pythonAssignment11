# 8. Write a python script to calculate sum of digits of a given number


n=int(input("Enter a number:"))
a=0
while n:
    a=a+n%10
    n=n//10
print("The first number of digit:",a)