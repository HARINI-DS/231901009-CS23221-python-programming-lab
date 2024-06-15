Given an integer N, check whether N the given number can be made a perfect square after adding 1 to it.
Input Format:
Single integer input.
Output Format:
Yes or No.
Example Input:
24
Output:
Yes
Example Input:
26
Output:
No
For example:
Input	Result
24	Yes
Program:
import math
a=int(input())
b=a+1
c=math.sqrt(b)
if(c==int(c)):
    print("Yes")
else:
   print("No")
