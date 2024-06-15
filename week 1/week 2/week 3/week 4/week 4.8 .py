Write a program that finds whether the given number N is Prime or not. If the number is prime, the program should return 2 else it must return 1.
Assumption: 2 <= N <=5000, where N is the given number.
Example1: if the given number N is 7, the method must return 2
Example2: if the given number N is 10, the method must return 1
For example:
Input	Result
7	2
10	1

Program:
a=int(input())
c=0
for i in range(2,a):
if(a%i==0):
c=1
if(c==1):
print("1")
elif(c==0): print("2”)
