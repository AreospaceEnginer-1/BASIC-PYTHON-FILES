
                           #start
             
nums = []     # assing empty lists for storing
ascending = []
decending = []
Value = None    #take one for taking and appending it to the list

while Value != 'stop':       #take numbers till stop comes
    Value = input('Enter stop to stop else enter a number: **')  # get input
    if Value != 'stop':  #see if value is not "stop"
        try:       #try to
                Value = int(Value)
        except TypeError: #if an error comes
                raise TypeError('Invalid Number... can\'t convert string to int')
        else: #if not
            Value = int(Value)  #convert to int
            nums.append(Value)       #add to nums

ascending = decending[:] = nums[:]    #copy it(because its mutable)
                
ascending.sort()  #  sort in ascending
decending.sort(reverse = True)  # sort in decending

print("Ascending order = ", ascending)  #show results
print("Decending order = ", decending)

                          #end


