
def is_leap(year):
  leap_year = False
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap_year = True
        return leap_year
        print("leap year")
      else:
        return leap_year
        print("not a leap year")
    else:
      leap_year = True
      return leap_year
      print("leap year")
  else:
    return leap_year
    print("not a leap year")


#TODO - Add more codes here
def days_in_month(input_year, input_month):
  """returns the days in a given year and month with leap year consideration"""
  #            JAN FEB MAR APR MAY JUN JUL AUG SEPT OCT NOV DEC
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_result = is_leap(input_year)
  if leap_result == True:
    month_days[1] = 29
  result_days = month_days[input_month - 1]
  return result_days 
    
days_in_month()
# Do not touch code below
year = int(input())
month = int(input())
days = days_in_month(year, month)
print (days)