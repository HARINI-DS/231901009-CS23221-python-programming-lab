Write a simple python program to find the square root of a given floating point number. The output should be displayed with 3 decimal places.
Sample Input:
8.00
Sample Output:
2.828
For example:
Input	Result
14.00	3.742

Program:
import math
a=float(input())
b=math.sqrt(a)
print(format(b,".3f"))
