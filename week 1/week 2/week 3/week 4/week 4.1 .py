Write a program to return the nth number in the fibonacci series. The value of N will be passed to the program as input.
NOTE: Fibonacci series looks like –
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, . . . and so on.
i.e. Fibonacci series starts with 0 and 1, and continues generating the next number as the sum of the previous two numbers.
• first Fibonacci number is 0,
• second Fibonacci number is 1,
• third Fibonacci number is 1,
• fourth Fibonacci number is 2,
• fifth Fibonacci number is 3,
• sixth Fibonacci number is 5,
• seventh Fibonacci number is 8, and so on.

For example:
Input	Result
1
4
7	0
2
8

Program:
a=int(input())
b=0
c=1
if(a==1):
     print("0")
elif(a==2):
       print("1")
else:
        for i in range (3,a+1):
              d=b+c
               b=c
               c=d
         print(d)
