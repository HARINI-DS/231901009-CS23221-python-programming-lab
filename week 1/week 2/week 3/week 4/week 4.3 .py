Given a positive integer N, check whether it can be represented as a product of single digit numbers.
Input Format:
Single Integer input.
Output Format:
Output displays Yes if condition satisfies else prints No.
Example Input:
14
Output:
Yes
Example Input:
13
Output:
No
Program:
a=int(input())
c=0
for i in range(1,10): for j in range(1,10):
if i*j==a:
c=1
if(c==1):
print("Yes")
else:
print("No")
