''' 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
Sample Output:
25
48 '''

add_num = lambda num:num + 15
print(add_num(10))
print(add_num(33))

multiply_num = lambda x,y:x * y
print(multiply_num(2,3))