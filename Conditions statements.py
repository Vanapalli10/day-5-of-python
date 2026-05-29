#Conditions statements
#Write a code to find out the greatest number between two numbers and you need to
#take input from the user and the inputs must and should be first- and second -number

'''first_number=int(input("enter the first number"))
second_number=int(input("enter the second number"))
if (first_number>second_number):
    print(f"first_number is greatest than the second number{first_number}")
else: 
    print(f"second_number is greater than the first_number{second_number}")
     
enter the first number30
enter the second number20
first_number is greatest than the second number30'''


#find out the number even or not the number should be taken from the User
#even
'''number=int(input("enter the number"))
if number%2==0:
    print("even")
else:
    print("not an odd")
o/p:enter the number8'''

'''#odd
number=int(input("enter the number"))
if number%2==1:
    print("odd")
else:
    print("not an odd")
    enter the number9
enter the number9
odd'''

'''#not equal to
number=int(input("ente the number"))
if number%2!=0:
    print("odd")
else:
    print("not an odd")
ente the number44
not an odd'''

#program to find out the given number is positive or negative or zero and 
#number should be taken from the input`
''' number=int(input("enter the number:"))
if number>0:
    print("positive")
elif number<0:
    print("negative")
else:
    print("zero")
enter the number:55
positive
enter the number:0
zero'''

#find out the largest number between the three numbers
'''first_number=int(input("enter the first number:"))
second_number=int(input("enter the second number:"))
third_number=int(input("enter the third number:"))
if (first_number>second_number and first_number>third_number):
    print("first number is the largest number")
elif(second_number>first_number and second_number>third_number):
    print("second number is the largest number")
else:
    print("third numberis the largest number")

 o/p: enter the first number:9
enter the second number:8
enter the third number:7
first number is the largest number'''


'''number=int (input("enter the number"))
if number%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

enter the number45
divisible by 5'''


#find the given year is leap year or not 
'''year=int(input("enter the year"))
if(year%4==0 and year%100!=0)or (year %400==0):
     print("leap year")
else:
    print("not leap year")

o/p:enter the year2026
not leap year'''

#A gym offers membership plans basec on the nymber of months enrolled
#Test case1
#input:3
#output:5000

#Test case2
#input:5
#output:9000

#Test case3
#input:-1
#output: invalid input

'''month=int(input("enter the month"))
if month<0:
    print("invalid input")
elif month==0:
    print(0)
elif month==1:
    print(2000)
elif month==2 or month==3:
    print(5000)
elif month>=4 and month<=6:
    print(9000)
elif month==9:
    print(12000)
elif month==12:
    print(15000)
else:
    print("error")
enter the month3
5000
enter the month5
9000
enter the month-1
invalid input'''

#calculate total parking fee based on number of hours
#test case: 1
#input:2
#output:200

#test case:2
#input:6
#output:370

#test case
#input:Six
#output:Error

'''try:
    hours=int(input("enter the number of hours"))

except:
    print("error")
if hours<=2:
    fee=hours*100
elif hours<5:
    fee=(2*100)+(hours-2)*50
else:
    fee=(2*100)+(3*50)+(hours-5)*20
    print(fee)

enter the number of hours5
350
enter the number of hours6
370'''


amount=int(input("enter the amount"))
if amount<1000:
    discount=0.05
elif 1000<= amount < 5000:
    discount=0.10
else:
    discount=0.15
final_amount=amount-(amount*discount)
print(f"final amount is{final_amount}")
print("final amount after two decimal points",round(final_amount,2))