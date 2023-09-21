#Name - Bhavya Amish Shah
#UCID - bs635
#Date - 21 September, 2023
#Attempting to convert negative values to positive ones.
a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n".format(num))
    print(arr)
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value

    #funct
    def convert_to_positive(x):
        if isinstance(x, (int, float)) and x < 0:        #this condition is for negative integers/float numbers
            return abs(x)
        elif isinstance(x, str) and x.startswith('-'):   #this condition is for string values
            return x[1:]
        else:                                            #this condition is for positive values
            return x

    positive_data=[]
    for x in arr:
        positive_data.append(convert_to_positive(x))     #calling to convert function for each value in the list

    print("\nPositive Output: \n{}".format(positive_data))   #printing the output
    print(type(positive_data[1]))                            #printing the type of the output
    
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)