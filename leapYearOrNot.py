"""ask user to input any year and print either its a leap year or not,

1.ask user to input any year and assign user input to variable with name year.
2.use if else condition,
   if year is divisible by 100 and 400 then print its a leap year
   if its divisible by 4 its a leap year 
   else its not a leap year.

   (we check if the year is leap year or not by two ways. one if its a century year it need
    to be divisible by 400 to be a leap year. or if its not a century year it needs to
     be divisible by 4 in order to be a leap year  )
"""

year=int(input("enter a year "))
if year%100==0 and year%400==0:
    print("its a leap year ")
elif year%4==0:
    print("its a leap year ")
else:

    print("its not a  leap year ")        