Write a program to find the sum of the series 1 +11 + 111 + 1111 + . . . + n terms (n will be given as input from the user and sum will be the output)
Sample Test Cases
Test Case 1      
Input
4          
Output
1234 
Explanation:
as input is 4, have to take 4 terms. 
1 + 11 + 111 + 1111
Test Case 2
Input 
6
Output 
123456
For example:
Input	Result
3	123
Program:
a=int(input())
t=1
s=0
for i in range(a)
    s+=t
     t=t*10+1
print(s)
