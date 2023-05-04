
def is_year():

    year_str = input("Enter a year: ")
   
    if not year_str.isdigit():
        print ("enter a digit number")
    else:    
        year = int(year_str)
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(" is a leap year")
        else:
            print(" not leap year")
        
is_year()
 

