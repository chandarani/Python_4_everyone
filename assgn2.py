Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the 
largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an 
appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.



largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        val = int(num)
    except:
        #print("Please enter a number as input or \'done\'")
        print("Invalid Input")
        continue

    if smallest is None or smallest > val:
        smallest = val
    if largest is None or largest < val:
        largest = val
   
    
def done(largest,smallest):
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))

done(largest,smallest)
