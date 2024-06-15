Write a program to calculate and print the Electricity bill where the unit consumed by the user is given from test case. It prints the total amount the customer has to pay. The charge are as follows: 
Unit                                                     Charge / Unit
Upto 199                                             @1.20
200 and above but less than 400        @1.50
400 and above but less than 600        @1.80
600 and above                                    @2.00
If bill exceeds Rs.400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.100/- 
Sample Test Cases
Test Case 1 
Input
50 
Output
100.00 
Test Case 2
Input 
300
Output 
517.50
For example:
Input	Result
100.00	120.00

Program:
a=float(input())
if(a<200):
    b=a*1.20
    if(b<=100):
        b=100
        print(format(b,".2f"))
    else:
        print(format(b,".2f"))
elif(a>=200 and a<400):
    c=a*1.50
    if(c>=400):
       print(format(c*0.15+c,".2f"))
    else:
       print(format(c,".2f")) 
elif(a>=400 and a<600):
    d=a*1.80
    print(format(d*0.15+d,".2f"))
elif(a>600):
    e=a*2.00
    print(format(e*0.15+e,".2f"))
