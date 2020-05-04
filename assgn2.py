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