#implemant a python program that determines whether the given year if elif statment
year=int(input("enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
  print("the year is a leap year!")
else:
  print("the leap year isn't a leap year!")