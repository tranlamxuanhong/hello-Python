#First day python
b="something"
#print function and len function - this is length of the string
print(len(b))

# Input function is to ask user input
name = input("Enter your username:")

print("Welcome" + name)

#operation
a = 15
b = 4
multiplication_result = a*b
print(multiplication_result)

exponential_result = a**b
print(exponential_result)


oneVar = 'This variable has one value'
onevar = 'And this one has another'
oNeVaR = 15
print("Hello World")


print(type(oNeVaR))

boolean = True
print(boolean)

a = 15
b = 5

#f-string. Put f before the first quotation in the print
print(f'the result of {a} divided by {b} is equal to {a/b}')

#string.format
print('the result of {} dvided by {} is equal to {}'.format(a,b,a/b))
#to print string and number together , using str()
print('test' + str(a))

#convert the input from string to int; same with float
input = "10"
print(int(input))

float_input = '2.2'
print(float(float_input))

#true boolean = 1
boolean_true = True
print(int(boolean_true))

#false boolean equal 0
boolean_false = False
print(int(boolean_false))

#transform to string
transform_to_string = True
print(str(transform_to_string))

#transform boolean to integer
print('True is evaluated as {} and false is evaluated as {}'.format(int(boolean_true),int(boolean_false)))

# Transform these variables to a numeric data type and add them together
a = True
b = '12'
c = '5.67'
d = int(a) + int(b) + float(c)
# Now, transform the result to a string. Make sure to assign the result to a new variable!
newVariable = str(d)

# Finally, print your result by editing the following print statement. Do not use a new print statement!
print('The result of the addition was...' + newVariable)

#List
fruit = ["coconut", "frape"]
print(fruit[0])

another_list = [True,'two',3.54, 4]
print(another_list)

#collection of key value pairs
players_number = {"football" : 11, "volleyball" : 5, "badminton" : 6}
print(players_number.get("football"))

#float variables

a = 5
b = 6
c = 7
d = 8

print(float(a)*float(b)*float(c)* float(d))

#concatunates or add these strings
string1 = "Data"
string2 = "Skills for"
string3 = " All"
print(string1 + string2 + string3)

#convert to int
my_string = "567"
convert_to_integer = int(my_string)
length_my_string = len(my_string)
result = convert_to_integer/length_my_string
print(int(result))
      