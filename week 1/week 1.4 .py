Alfred buys an old scooter for Rs. X and spends Rs. Y on its repairs. If he sells the scooter for Rs. Z (Z>X+Y). Write a program to help Alfred to find his gain percent. Get all the above-mentioned values through the keyboard and find the gain percent.
Input Format:
The first line contains the Rs X
The second line contains Rs Y
The third line contains Rs Z
Sample Input:
10000
250
15000
Sample Output:
46.34 is the gain percent.

For example:
Input	Result
45500
500
60000	30.43 is the gain percent.
Program:
a=int(input())
b=int(input())
c=int(input())
d=a+b
e=c-d
f=(e/d)*100
print(format(f,".2f"),"is the gain percent.")
