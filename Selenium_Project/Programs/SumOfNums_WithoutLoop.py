
# Using recursive method to sum all the numbers from an input list.
def recursive_sum(input_list):
    if len(input_list) == 0:
        return  0
    else:
        return input_list[0] + recursive_sum(input_list[1:])

list = [1,2,3,4,5]
print(recursive_sum(list))

# Using recursion method add the first 'n' numbers
def recursive_sum_1(input_number):
    if input_number == 0:
        return 0
    else:
        return input_number + recursive_sum_1(input_number - 1)

print(recursive_sum_1(5))
