# 7. Write a python script to count digits in a given number



n=int(input("Enter a number:"))
a=1
while(n>0):
    a=a+1
    n=n//10
print("The first number of digit:",a)