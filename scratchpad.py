input_year = int(input())
century_year = False
if input_year % 100 == 0:
    century_year = True
if input_year % 400 == 0 and century_year == True:
    is_leap_year = True
    result = "leap year"
elif input_year % 4 == 0 and century_year == False:
    is_leap_year = True
    result = "leap year"
else:
    is_leap_year = False
    result = "not a leap year"
print(f"{input_year} - {result}")
print(input_year % 4)