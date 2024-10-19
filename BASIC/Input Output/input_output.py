# input ---> refers to take data from the user using intput() function as a string.
# output --> Display the data on the screen using print() function

name = input("Enter Your name:")
print(name) 

print("\n========problem with input() function==============")

# 

num1 = input("Enter first number:")  # 3
num2 = input("Enter second number:") # 3
print(num1+num2) # output = 33  

# but we want 3+3 = 6 

print("\n================Eval Function=====================")

num1 = eval(input("Enter first number:"))  # 3
num2 = eval(input("Enter second number:")) # 3
print(num1+num2) # output = 6
