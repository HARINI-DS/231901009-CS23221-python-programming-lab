A Number is said to be Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. Write a program to print number is Disarium or not.
Input Format:
Single Integer Input from stdin.
Output Format:
Yes or No.
Example Input:
175
Output:
Yes
Explanation
1^1 + 7^2 +5^3 = 175
Example Input:
123
Output:
No
For example:
Input	Result
175	Yes
123	No
Program:
a=input()
n=len(a)
r=0
for i,d in enumerate(a): 
     r+=int(d)**(i+1)
     if r==int(a):
        print("Yes")
    else:
          print("No")
