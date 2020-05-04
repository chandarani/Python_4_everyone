Write a program to prompt the user for hours and rate per hour using the input to compute gross pay. Use 35 hours and a rate of 2.75 per
hour to test the program (the pay should be 96.25). You should use the input to read a string and float() to convert the string to a
number. Do not worry about error checking or bad user data.

                                                        or
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 
40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the
pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error 
checking the user input - assume the user types numbers properly.




def computepay(h,r):
    if h > 40:
        p = (40 * r) + ((h - 40) * 1.5 * r)
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
