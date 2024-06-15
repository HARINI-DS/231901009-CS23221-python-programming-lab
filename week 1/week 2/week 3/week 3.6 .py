The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown in the table below. The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.
Year Animal
2000 Dragon
2001 Snake
2002 Horse
2003 Sheep
2004 Monkey
2005 Rooster
2006 Dog
2007 Pig
2008 Rat
2009 Ox
2010 Tiger
2011 Hare
Write a program that reads a year from the user and displays the animal associated with that year. Your program should work correctly for any year greater than or equal to zero, not just the ones listed in the table.
Sample Input 1
2010
Sample Output 1
2010 is the year of the Tiger.
Sample Input 2
2020
Sample Output 2
2020 is the year of the Rat.
Program:
a=int(input())
b=a%12 
if(b==0):
    print(a,"is the year of the Monkey.")
elif(b==1):
    print(a,"is the year of the Rooster.")
elif(b==2):
    print(a,"is the year of the Dog.")
elif(b==3):
    print(a,"is the year of the Pig.")
elif(b==4):
    print(a,"is the year of the Rat.")
elif(b==5):
    print(a,"is the year of the Ox.")
elif(b==6):
    print(a,"is the year of the Tiger.")
elif(b==7):
    print(a,"is the year of the Hare.")
elif(b==8):
    print(a,"is the year of the Dragon.")
elif(b==9):
    print(a,"is the yaer of the Snake.")
elif(b==10):
    print(a,"is the year of the Horse.")
elif(b==11):
    print(a,"is the year of the Sheep.")
