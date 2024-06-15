Write a program to convert strings to an integer and float and display its type.
Sample Input:
10
10.9
Sample Output:
10,<class 'int'>
10.9,<class 'float'>

For example:
Input	Result
10
10.9	10,<class 'int'>
10.9,<class 'float'>

Program:
a=int(input())
print(a,end=",")
print(type(a))
b=float(input())
print(round(b,1),end=",")
print(type(b)
