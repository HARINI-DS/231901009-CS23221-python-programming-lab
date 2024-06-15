Three numbers form a Pythagorean triple if the sum of squares of two numbers is equal to the square of the third.
For example, 3, 5 and 4 form a Pythagorean triple, since 3*3 + 4*4 = 25 = 5*5 
You are given three integers, a, b, and c. They need not be given in increasing order. If they form a Pythagorean triple, then print "Yes", otherwise, print "No". 
Sample Input
3
5
4
Sample Output
yes
Sample Test Cases
Test Case 1     
Input
3
5
4
Output
yes
Test Case 2     
Input
5
8
2
Output
no
 
Program:
a=int(input())
b=int(input())
c=int(input())
if(a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b):
    print("yes")
else:
    print("no")
