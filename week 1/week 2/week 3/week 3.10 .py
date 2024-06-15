Write a program to find the eligibility of admission for a professional course based on the following criteria:
Marks in Maths >= 65
Marks in Physics >= 55
Marks in Chemistry >= 50
Or
Total in all three subjects >= 180
Sample Test Cases
Test Case 1
Input
70
60
80
Output 
The candidate is eligible
Test Case 2 
Input
50
80
80 
Output
The candidate is eligible
Test Case 3
Input
50
60
40
Output
The candidate is not eligible
For example:
Input	Result
50
80
80	The candidate is eligible
50
80
80	The candidate is eligible

Program:
a=int(input())
b=int(input())
c=int(input())
if(a>=65 and b>=55 and c>=50):
    print("The candidate is eligible")
elif(a+b+c>=180):
    print("The candidate is eligible")
else:
    print("The candidate is not eligible")
