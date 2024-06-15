Given a number N, find the next perfect square greater than N.
Input Format:
Integer input from stdin.
Output Format:
Perfect square greater than N.
Example Input:
10
Output:
16

Program:
import math
a=int(input())
b = a + 1
while b > 0 :
   m=math.sqrt(b)
   if(m==int(m)):
      print(b)
      break
   else:
      b = b + 1
