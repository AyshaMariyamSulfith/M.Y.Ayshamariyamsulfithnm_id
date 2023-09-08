def is_leap(year):
     if (year%4==0 and year%100!=0):
       return true
     elif ( year%400==0):
         return True
     else:
         return False
year= int(input("Enter a year"))
if is_leap(year):
    print("{ } is leap year".format(year))
else:
      print("{} is not a leap year".format(year))