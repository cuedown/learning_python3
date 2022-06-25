import string
print("Hello World") #this line prints hello world
print(500) #this line prints 500
# is for single line comments
# needs one at every line if u want multiple line comments
"""this is a multi
line
break
cool for long comments
w/out any worry"""
string_test='''we can use these 
for multiple
line strings''' #sets multi line string
print(string_test) #prints seperate lines defined by the above string
print(len(string_test)) #prints the length of characters within string_test variable
# indexing starts at 0; so value of HELLO, H is 0 and the O is 4 (n-1 where n is the length of the value)
# indexing is used with [] connotation for variables and other uses
first_letter=string_test[0] #creates a variable for the first letter of string_test
print(first_letter) #prints the first letter of string_test
last_letter=string_test[41] # we found length of string_test on line 17 (its 42) therefore last letter is 41 (n-1 where n is 42)
print(last_letter)# prints the last letter of string_test
#or we can not set a variable for it
print(string_test[0])
#reverse indexing works too..
print(string_test[-1]) #prints the last letter of the variable (0 is the start, -1 is the last, -2 second last, etc)
print(string_test[-2]) #prints second last letter 
none_var=None #sets Nonetype variable to none_var
print(none_var) #prints None
print(type(none_var)) #prints what type of variable class none_var is
"""None is not a default value for the variable that has not yet been assigned a value.
None is not the same as False.
None is not an empty string.
None is not 0."""
#next up is slicing... Slicing is the process of obtaining a portion (substring) of a string by using its indices.
#Given a string, we can use the following template to slice it and obtain a substring: string[start:end]
# where start is the index from where we want the substring to start.
# end is the index where we want our substring to end.
string_splice="this is a splice test" # defines string we are splicing in next step
print(string_splice[0:4]) # From the start till before the 4th index
print(string_splice[1:7]) # from the 1 index (which is the second letter; index starts at 0) to the 7th index (8th letter)
print(string_splice[8:len(string_splice)]) # From the 8th index till the last index
"""string[start:end:step] allows us to slice a string by defining a step through which we can skip characters in the string. 
The default step is 1, so we "skip" through the string one character at a time.
if you change to 2, it skips every other, 5, every fifth iteration
"""
line_break="" # string that is blank
print(line_break) #prints a blank line
print(string_splice[0:7])  # A "step" of 1 (default)
print(string_splice[0:7:2])  # A "step" of 2 (lists every other value starting with 1st value (iteration 0))
print(string_splice[0:7:5])  # A "step" of 5 (prints every 5th value starting with 1st value (iteration 0))
#Reverse Slicing - Strings can also be sliced to return a reversed substring.
# In this case, we would need to switch the order of the start and end indices (string[end:start])
# A negative step must also be provided
print(line_break) #line break
print(string_splice[13:2:-1]) # start at 3rd value (2nd indice) and list backwards to finish at 13th indice (14th value)
print(string_splice[len(string_splice):0:-1]) # lists backwards from end to start (skips first indice value)
print(string_splice[len(string_splice):0:-2]) # Take 2 steps back. The opposite of what happens in the slide above
"""Partial Slicing #
One thing to note is that specifying the start and end indices is optional.
If start is not provided, the substring will have all the characters until the end index.
If end is not provided, the substring will begin from the start index and go all the way to the end."""
print(line_break) #line break
print(string_splice[:8])  # All the characters before the 8th indice (9th value of string)
print(string_splice[8:])  # All the characters starting from 8th indice
print(string_splice[:])  # The whole string
print(string_splice[::-1])  # The whole string in reverse (step is -1)
"""String formatting means substituting values into a string. Following are some use cases of string formatting:
Inserting strings within a string
Inserting integers within a string
Inserting floats within a string"""
string1 = "I like %s" % "Python" #   %s is the format specifier, which tells Python to insert the text here. 
# Python will insert a string if:
# We follow the string with a % and another string.
# We follow the string with a % and another string type variable.
print(string1) # prints 'I like Python'
temp = "Educative" #sets a string variable to text
string2 = "I like %s" % temp # setting a string within string
print(string2) # prints 'I like Educative'
string3 = "I like %s and %s" % ("Python", temp) #sets up a string, with a string within a string (uses first-in-first-out method)
print(string3)  # 'I like Python and Educative'
# integers within a string
string_int = "%i + %i = %i" % (1,2,3) # The %i is the format specifier, which tells Python to insert the integers here.
print(string_int) # prints '1 + 2 = 3'
# Inserting Floats Within a String
stringfloat = "%f" % (1.11) #includes zeros
print(string1) # prints '1.110000'
stringfloat2 = "%.2f" % (1.11) #caps at 2 decimal points
print(string2) # prints '1.11'
stringfloat3 = "%.2f" % (1.117) #caps at 2 decimal points (it rounds up)
print(string3) # prints '1.12'
"""Operators are used to perform arithmetic and logical operations on data. They enable us to manipulate and interpret data to produce useful outputs.
Operators are represented by characters or special keywords.
In general, Pythons operators follow the or prefix notations. operators appear between two operands (values on which the operator acts) and hence, are usually known as binary operators
A prefix operator usually works on one operand and appears before it. Hence, prefix operators are known as unary operators
The 5 main operator types in Python are:
arithmetic operators
comparison operators
assignment operators
logical operators
bitwise operators"""
#arithmetic operators
# ** is exponent
# * is multiplicative
# % is modulo
# / is division
# // is floor division
# + is addition
# - is subtraction
# () is parenthesis for equations
#
# addition
print(10 + 5)
float1 = 13.65
float2 = 3.40
print(float1 + float2)
num = 20
flt = 10.5
print(num + flt)
"""Python automatically converts the integer to a floating-point number. 
This applies to all arithmetic operations."""
# subtraction
print(10 - 5)
float1 = -18.678
float2 = 3.55
print(float1 - float2)
num = 20
flt = 10.5
print(num - flt)
# multiplication
print(40 * 10)
float1 = 5.5
float2 = 4.5
print(float1 * float2)
print(10.2 * 3)
# division
print(40 / 10)
float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2)
# floor division
"""In floor division, the result is floored to the nearest smaller integer. 
It is also known as integer division."""
print(43 // 10)
float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)
print(line_break) #line break
# Unlike normal division, floor division between two integers results in an integer.
# modulo
# modulo is the remainder of two numbers divided by each other. (5mod2 is 1 because 5 is divisible by 2, twice, with 1 left over)
print(10 % 2)
twenty_eight = 28
print(twenty_eight % 10) # 28mod10 = 8
print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
print(28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float as well
# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction
# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication
print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))
# Comparison operators can be used to compare values in mathematical terms.
"""
>	Greater Than
<	Less Than
>=	Greater Than or Equal To
<=	Less Than or Equal To
==	Equal To
!=	Not Equal To
is	Equal To (Identity)
is not	Not Equal To (Identity)
#
The result of a comparison is always a bool. If the comparison is correct, the value of the bool will be True. 
Otherwise, its value will be False. The == and != operators compare the values of both operands. 
However, the identity operators, is and is not, check whether the two operands are the exact same object, not values within them"""
num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]
print(num2 > num1)  # 10 is greater than 5 = true
print(num1 > num2)  # 5 is not greater than 10 = false
print(num2 == num3)  # Both have the same value = true
print(num3 != num1)  # Both have different values = true
print(3 + 10 == 5 + 5)  # Both are not equal = false
print(3 <= 2)  # 3 is not less than or equal to 2 = false
print(num2 is not num3)  # Both have the same object = false
print(list1 is list2)  # Both have the different objects = false
# Assignment Operators
""" The = operator is an assignment operator, but not the only one.
=	Assign
+=	Add and Assign
-=	Subtract and Assign
*=	Multiply and Assign
/=	Divide and Assign
//=	Divide, Floor, and Assign
**=	Raise power and Assign
%=	Take Modulo and Assign
|=	OR and Assign
&=	AND and Assign
^=	XOR and Assign
>>=	Right-shift and Assign
<<=	Left-shift and Assign
"""
year = 2019
print(year)
year = 2020
print(year)
year = year + 1  # Using the existing value to create a new one
print(year)
"""when a variable, first, is assigned to another variable, second, its value is copied into second. 
Hence, if we later change the value of first, second will remain unaffected:"""
first = 20
second = first
first = 35  # Updating 'first' value
print(first, second)  # 'second' remains unchanged
print(line_break) #linebreak
num = 10 #sets as 10
print(num)
num += 5 # add + assign, so 5+10 assigns 15
print(num)
num -= 5 # subtract + assign so 5-15 assigns 10
print(num)
num *= 2 #multiply and assign = 20
print(num)
num /= 2 #divide and assign = 10
print(num)
num **= 2 # raise to the power of 2 and assign = 100
print(num)
"""Logical operators are used to manipulate the logic of Boolean expressions.
and	AND
or	OR
not	NOT	Prefix
"""
print(line_break)
# OR Expression
my_bool = True or False
print(my_bool)
# AND Expression
my_bool = True and False
print(my_bool)
# NOT expression
my_bool = False
print(not my_bool)
# in bit terms, the value of True is 1. False corresponds to 0:
print(10 * True) #prints 10x1
print(10 * False) #prints 10x0
"""
In programming, all data is actually made up of 0s and 1s known as bits. Bitwise operators allow us to perform bit-related operations on values.

Operator	 Purpose
&	        Bitwise  AND
|	        Bitwise  OR
^	        Bitwise  XOR
~	        Bitwise  NOT
<<	        Shift Bits Left
>>	        Shift Bits Right
"""
num1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100
print(num1 & num2)   #prints 0   -> Binary value = 00000
print(num1 | num2)   #prints 30  -> Binary value = 11110
print(num1 ^ num2)   #prints 30  -> Binary value = 11110
print(~num1)         #prints -11 -> Binary value = -(1011)
print(num1 << 3)     #prints 80  -> Binary value = 0101 0000
print(num2 >> 3)     #prints 2   -> Binary value = 0010
"""Comparison Operators
Strings are compatible with the comparison operators. Each character has a Unicode value.

This allows strings to be compared on the basis of their Unicode values.

When two strings have different lengths, the string which comes first in the dictionary is said to have the smaller value.

Lets look at a few examples:"""
print('a' < 'b')  # 'a' has a smaller Unicode value than 'b' = true
house = "Gryffindor"
house_copy = "Gryffindor"
print(house == house_copy) # = true
new_house = "Slytherin"
print(house == new_house) # = false
print(new_house <= house) # = false
print(new_house >= house) # = true
"""Concatenation
The + operator can be used to merge two strings together:"""
first_half = "Bat"
second_half = "man"

full_name = first_half + second_half
print(full_name) #prints batman
"""The * operator allows us to multiply a string, resulting in a repeating pattern:"""
print("ha" * 3) #prints hahaha
"""Search
The in keyword can be used to check if a particular substring exists in another string. If the substring is found, the operation returns true.
Heres how it works:"""
random_string = "This is a random string"
print('of' in random_string)  # Check whether 'of' exists in randomString
print('random' in random_string)  # 'random' exists!
"""In Python, we can store multiple values together in a single variable. While there are many ways of doing so, the most popular is the list.
It is very similar to a string since a string is a collection of characters. A list is also just a collection of values. However, the values can be of any type.
All we have to do is enclose all the elements in square brackets, [], and separate them with commas."""
my_list = [1, 2.5, "A string", True]
print(my_list)
# It’s as simple as that! Lists can be indexed and sliced just like strings. The len command works with them too:
my_list = [1, 2.5, "A string", True]
print(my_list[2])
print(len(my_list))
"""Problem Statement#
Gravitational force is the attractive force that exists between two masses. It can be calculated by using the following formula:
G*M*m / r^2
where G is the gravitational constant, M and m are the two masses, and r is the distance between them.
You must implement this equation in Python to calculate the gravitational force between Earth and the moon."""
G = 6.67 * (10 ** -11) #grav constant
M = 6.0 * (10 ** 24)  # Mass of Earth
m = 7.34 * (10 ** 22)  # Mass of the moon
r = 3.84 * (10 ** 8) #distance between them
# Write your code here
grav_force = (G * M * m) / (r ** 2)
print(grav_force)



"""A conditional statement is a Boolean expression that, if True, executes a piece of code.

It allows programs to branch out into different paths based on Boolean expressions result in True or False outcomes."""
# conditional statements
# if true then x if false then y
"""
if conditional_statement is True:
    # execute expression1
    pass
else:
    # execute expression2
    pass
"""
"""There are three types of conditional statements in Python:

if
if-else
if-elif-else
"""
# if-statement
"""The simplest conditional statement that we can write is the if statement. It comprises of two parts:

The condition
The code to be executed
An if statement runs like this:

if the condition holds True, execute the code to be executed. Otherwise, skip it and move on."""
num = 5

if (num == 5):  # The condition is true
    print("The number is equal to 5")  # The code is executed

if num > 5:  # The condition is false so wont print anything
    print("The number is greater than 5")  # The code is not executed as its false in line above
"""
the print command inside the body of the if statement is indented to the right. If it wasnt, there would be an error. 

    Indentation

Indentation plays an essential role in Python. Statements with the same level of indentation belong to the same block of code. 
The code of an if statement is indented a space further than the code outside it in order to indicate that this is an inner and inter-related block.
The convention of our indents must also be consistent throughout a block. If we have used two spaces to make an indent,
we must use two spaces for an indent in the same block. Hence, always keep indentation in mind when writing code."""
print(line_break)
num = 12

if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    # Only works when num is a multiple of 2, 3, and 4
    print("The number is a multiple of 2, 3, and 4")

if (num % 5 == 0 or num % 6 == 0):
    # Only works when num is either a multiple of 5 or 6
    print("The number is a multiple of 5 and/or 6")
"""
in the first if statement, all the conditions have to be fulfilled since were using the "and" operator.

in the second if statement, the Boolean expression would be true if either or both of the clauses are satisfied because we are using the "or" operator.
"""
print(line_break)
# nested IF's
num = 63

if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")
            #Each nest if statement requires further indentation.
"""
Creating and Editing Values
In a conditional statement, we can edit the values of our variables.

Furthermore, we can create new variables."""
num = 10
if num > 5:
    num = 20  # Assigning a new value to num
    new_num = num * 5  # Creating a new value called new_Num

# The if condition ends, but the changes made inside it remain
print(num)
print(new_num)


# if - else
num = 60

if num <= 50:
    print("The number is less than or equal to 50")
else:
    print("The number is greater than 50")
"""
If the condition turns out to be False, the code after the else: keyword is executed.

Hence, we can now perform two different actions based on the conditions value.

The else keyword will be on the same indentation level as the if keyword. Its body will be indented one tab to the right just like the if statement."""
# it can be written like this too
num = 60

if num <= 50:
    print("The number is less than or equal to 50")

if num > 50:
    print("The number is greater than 50")
"""However, for the second if, we have to specify the condition again. 
This can be tricky when dealing with complex conditions. 
The else statement automatically handles all the situations when the if fails."""



"""
Conditional expressions use the functionality of an if-else statement in a different way.

The expression returns an output based on the condition we provide. This output can be stored in a variable.

A conditional expression can be written in the following way:

output_value1 if condition else output_value2

If the if condition is fulfilled, the output would be output_value1. Otherwise, it would be output_value2.

Lets refactor the previous if-else statement into a conditional expression:"""
print(line_break)
num = 60

output = "The number is less than or equal to 50" \
    if num <= 50 else "The number is greater than 50"

print(output)
# Please note that the backslash \ in the above code is only a line continuation character that can be used to split a single line into multiple lines.
"""
The if-else statement handles two sides of the same condition: True and False. This works very well if were working with a problem that only has two outcomes.

However, in programming, it isnt always a True or False scenario, and a problem can have multiple outcomes.

This is where the if-elif-else statement shines. It is the most comprehensive conditional statement because it allows us to create multiple conditions easily.

The elif stands for else if, indicating that if the previous condition fails, try this one.
"""
light = "Red" #sets light value to red

if light == "Green": #first if statement prints if green
    print("Go")

elif light == "Yellow": # if not green, it will check yellow next (elif) and print caution if yellow
    print("Caution")

elif light == "Red": #if not green or yellow, it will check red (elif) and print stop if red
    print("Stop")

else:
    print("Incorrect light signal") # if its not green, yellow, or red, its an incorrect input and will print this (final step)
#An if-elif statement can exist on its own without an else block at the end. 
#However, an elif cannot exist without an if statement preceding it
num = 5

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")
"""
An important thing to keep in mind is that an if-elif-else or if-elif statement is not the same as multiple if statements. if statements act independently.

If the conditions of two successive ifs are True, both statements will be executed.

On the other hand, in if-elif-else, when a condition evaluates to True, the rest of the statements conditions are not evaluated.

We will understand this better through an example:"""
print(line_break)

num = 10

if num > 5:
    print("The number is greater than 5")

if num % 2 == 0:
    print("The number is even")

if not num % 2 == 0:
    print("The number is odd")

# versus
print("versus")

num = 10

if num > 5:
    print("The number is greater than 5")

elif num % 2 == 0:
    print("The number is even")

else:
    print("The number is odd and less than or equal to 5")
"""As we can see, in the if tab, all the statements are computed one by one. Hence, we get multiple outputs.
In the if-elif-else tab, since the first condition holds true, all the others are discarded. 
This proves to be more efficient in terms of code performance."""


"""

Problem Statement #
In this challenge, you must discount a price according to its value.

If the price is 300 or above, there will be a 30% discount.

If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.

If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.

If the price is less than 100, there will be a 5% discount.

If the price is negative, there will be no discount."""
print(line_break)

price = 250

if price >= 300:
    price *= 0.7  # (1 - 0.3)
elif price >= 200:
    price *= 0.8  # (1 - 0.2)
elif price >= 100:
    price *= 0.9  # (1 - 0.1)
elif price < 100 and price >= 0:
    price *= 0.95  # (1 - 0.05)
elif price < 0:
    print("no discount")
print(price)
"""
Notice that we only need to specify the lower bound in each condition. This is because, for every condition, the upper bound is already being checked in the previous condition.

The program will only go into the first elif if the price is lower than 300.

This sort of smart structuring in a conditional statement can be very useful when dealing with a large number of complex cases.

The price after a discount would be price * (1 - discount)."""

# functions
"""Suppose we want to find the smaller value between two integers:"""
num1 = 10
num2 = 40
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)

num1 = 250
num2 = 120
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)

num1 = 100
num2 = 100
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)
"""
For every new pair of integers, we need to write the if-else statement again.

All this could become much simpler if we had a function to perform the steps necessary for calculating the minimum.

The good news is that Python already has the min() function:"""
minimum = min(10, 40)
print(minimum)

minimum = min(10, 100, 1, 1000)  # It even works with multiple arguments
print(minimum)

minimum = min("Superman", "Batman")  # And with different data types
print(minimum)
"""
Types of Functions in Python
Functions are perhaps the most commonly used feature of Python. There are two basic types of functions in Python:

Built-in functions
User-defined functions
We have already seen some instances of built-in function such as len(), min(), and print().

In Python, a function can be defined using the def keyword in the following format:

def function name (parameters):

The function name is simply the name we will use to identify the function.

The parameters of a function are the inputs for that function. 
We can use these inputs within the function. 
Parameters are optional. 
We will get to know more about these later.

The body of the function contains the set of operations that the function will perform. This is always indented to the right."""
def my_print_function():  # No parameters
    print("This")
    print("is")
    print("A")
    print("function")
# Function ended


# Calling the function in the program multiple times
my_print_function()
my_print_function()
"""Parameters are a crucial part of the function structure.

They are the means of passing data to the function. This data can be used by the function to perform a meaningful task.

When creating a function, we must define the number of parameters and their names. 
These names are only relevant to the function and wont affect variable names elsewhere in the code. 
Parameters are enclosed in parentheses and separated by commas.

The actual values/variables passed into the parameters are known as arguments.

we saw the min() function. It requires two numbers as inputs and prints the smaller one.

Lets define our own basic form of the min() function that simply prints the minimum. We will name it minimum():"""
def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num1 = 10
num2 = 20

minimum(num1, num2)
"""So far, weve only defined functions that print something. They dont return anything back to us. 
But if we think back, functions return values all the time. Just take len() for example. 
It returns an integer which is the length of the data structure.

To return something from a function, we must use the return keyword. 
Keep in mind that once the return statement is executed, the compiler ends the function. 
Any remaining lines of code after the return statement will not be executed.

Lets refactor the minimum() method to return the smaller value instead of printing it. 
Now, itll work just like the built-in min() function with two parameters:"""
def minimum(first, second):
    if (first < second):
        return first
    return second


num1 = 10
num2 = 20

result = minimum(num1, num2)  # Storing the value returned by the function
print(result)
"""In Python, data created inside the function cannot be used from the outside unless it is being returned from the function.

Variables in a function are isolated from the rest of the program. When the function ends, they are released from memory and cannot be recovered.

The following code will never work:
def func():
    name = "Stark"

func()
print(name)  # Accessing 'name' outside the function returns error "name not defined" 

Altering Data
When mutable data is passed to a function, the function can modify or alter it. 
These modifications will stay in effect outside the function scope as well. An example of mutable data is a list.

In the case of immutable data, the function can modify it, but the data will remain unchanged outside the functions scope. 
Examples of immutable data are numbers, strings, etc.

Lets try to change the value of an integer inside a function:"""
num = 20


def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num) # prints 200 within the function
    return n


multiply_by_10(num)
print("Value of num outside function:", num)  # The original value remains unchanged (prints 20 outside the function)
"""If we really need to update immutable variables through a function, we can simply assign the returning value from the function to the variable.
Now, we will try updating a mutable object through a function:"""
num_list = [10, 20, 30, 40]
print(num_list) # prints 10,20,30,40


def multiply_by_10(my_list): # sets function to multiply each value by 10
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


multiply_by_10(num_list) # runs function which updates values of the num_list
print(num_list)  # The contents of the list have been changed (100,200,300,400)
print(line_break)

"""We passed num_list to our function as the my_list parameter.
Now, any changes made to my_list will reflect in num_list outside the function.
This would not happen in the case of an immutable variable.




Functions that are properties of a particular entity are known as methods.
These methods can be accessed using the . operator.
The string data type has several methods associated with it. Lets look at some of them.
Search#
An alternative for finding a substring using the in keyword is the find() method.
It returns the first index at which a substring occurs in a string.
If no instance of the substring is found, the method returns -1.

-1 is a conventional value that represents a None or failure in case the output was supposed to be positive.

For a string called a_string, find() can be used in the following way:

a_string.find(substring, start, end)

substring is what we are searching for.
start is the index from which we start searching in a_string.
end is the index where we stop our search in a_string.
start and end are optional.
"""
random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range
print(line_break)

"""Replace
The replace() method can be used to replace a part of a string with another string. Heres the template we must use:

a_string.replace(substring_to_be_replaced, new_string)

The original string is not altered. Instead, a new string with the replaced substring is returned."""
a_string = "Welcome to Educative!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)
print(line_break)

"""Changing the Letter Case #
In Python, the letter case of a string can be easily changed using the upper() and lower() methods.

Lets try them out:"""
print("UpperCase".upper()) # prints UPPERCASE
print("LowerCase".lower()) # prints lowercase
print(line_break)

"""Joining strings
With join() method you can join multiple strings. Lets try it out:"""
list1 = ['a', 'b', 'c']
print('>>'.join(list1)) # joining strings with >>
print('<<'.join(list1)) # joining strings with <<
print(', '.join(list1)) # joining strings with comma and space
print(line_break)

"""Formatting
The format() method can be used to format the specified value(s) and insert them in strings placeholder(s). Lets try it out:"""
string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)
print(line_break)

"""The placeholders can be identified using named indexes {cname}, numbered indexes {0}, or even empty placeholders {}.


converting data

To convert data into an integer, we can use the int() utility.

Keep in mind, a string can only be converted to an integer if it is made up of numbers.
"""
print(int("12") * 10)  # String to integer
print(int(20.5))  # Float to integer
print(int(True))  # Bool to integer (true = 1 false = 0)
print(line_break)

# print (int("Hello")) # This wouldn't work!


# ord() function can be used to convert a character to its Unicode value:
print(ord('a'))
print(ord('0'))
print(line_break)

# The float() function translates data into a floating-point number:
print(float(24))
print(float('24.5'))
print(float(True))
print(line_break)

# To convert data into a string, we must use str():
print(str(12) + '.345')
print(str(False))
print(str(12.345) + ' is a string')
print(line_break)

# bool() function takes in data and gives us the corresponding Boolean value.
# Strings are always converted to True, except if the string is empty. 
# Floats and integers with a value of zero are considered to be False in Boolean terms:
print(bool(10))
print(bool(0.0))
print(bool("Hello"))
print(bool(""))
print(line_break)

"""The input() function
In Python, input() function is used to take input from user.

The input is automatically converted to string. If you enter a number, it will also be converted to a string.

Example
Below is an executable asking for users name as an input.
name = input("What is your name? ")
print("\nHello,", name) #\n is just a new line """


"""So far, weve always given names to our functions using the def keyword. 
However, there is a special class of functions for which we do not need to specify function names.

Definition
A lambda is an anonymous function that returns some form of data.

Lambdas are defined using the lambda keyword. Since they return data,
it is a good practice to assign them to a variable.

The following syntax is used for creating lambdas:

lambda parameters : expression

parameters seperated by commas, and expression is an operation that returns something

In the structure above, the parameters are optional.

Lets try creating a few simple lambdas.

Below, we can find a lambda that triples the value of the parameter and returns this new value:"""
triple = lambda num : num * 3  # Assigning the lambda to a variable

print(triple(10))  # Calling the lambda and giving it a parameter
# Here’s a simple lambda that concatenates the first characters of three strings together:
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print(concat_strings("World", "Wide", "Web"))
print(line_break)

"""As we can see, lambdas are simpler and more readable than normal functions. 
But this simplicity comes with a limitation.

A lambda cannot have a multi-line expression. 
This means that our expression needs to be something that can be written in a single line.

Hence, lambdas are perfect for short, single-line functions.

We can also use conditional statements within lambdas:"""
my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(60))
print(line_break)

"""When using conditional statements in lambdas, the if-else pair is necessary. 
Both cases need to be covered, otherwise, the lambda will throw an error

The Purpose of Lambdas
So, what is the point of having lambdas around? 
Were still assigning them to variables, so they do have names.

They can be written in-line, but that isnt a huge advantage.

Well, lambdas are really useful when a function requires another function as its argument.
In Python, one function can become an argument for another function. This is useful in many cases.

Lets make a calculator function that requires the add, subtract, multiply,
or divide function along with two numbers as arguments.

For this, we will have to define the four arithmetic functions as well."""
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))
print(line_break)

"""Using Lambdas
In the last lesson, we were discussing the purpose of lambdas. Well, now its their time to shine.

For the calculator method, we needed to write four extra functions that could be used as the argument.
This can be quite a hassle.

Why dont we just pass a lambda as the argument?
The four operations are pretty simple, so they can be written as lambdas.

Lets try it:"""
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)

print(calculator(lambda n1, n2: n1 + n2, 10, 20))
print(line_break)

"""The code looks much shorter now! We can define the operation on the go whenever we want.

This is the beauty of lambdas. They work really well as arguments for other functions.

More Examples#
The built-in map() function creates a map object using an existing list and a function as its parameters. This object can be converted to a list using the list() function (more on this later).

The template for map() is as follows:

map(function, list)

The function will be applied, or mapped, to all the elements of the list.

Below, we will use map() to double the values of an existing list:"""
num_list = [0, 1, 2, 3, 4, 5]

double_list = map(lambda n: n * 2, num_list)

print(list(double_list))
print(line_break)

"""This creates a new list. The original list remains unchanged.

We could have created a function that doubles a number and used it as the argument in map()
but the lambda made things simpler.

Another similar example is the filter() function. It requires a function and a list.

filter() filters elements from a list if the elements satisfy the condition that is specified in the argument function.

Lets write a filter() function that filters all the elements which are greater than 10:"""
numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n: n > 10, numList))
print(greater_than_10)
print(line_break)

"""The function returns a filter object which can be converted to a list using list().

just like map(), filter() returns a new object without changing the original list.

Recursion is the process in which a function calls itself during its execution. 
Each recursive call takes the program one scope deeper into the function.

The recursive calls stop at the base case. 
The base case is a check used to indicate that there should be no further recursion.

Imagine recursive calls as nested boxes where each box represents a function call. 
Each call makes a new box. When the base case is reached, we start moving out of the boxes one by one:"""
def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print(number)


rec_count(5) # prints 5,4,3,2,1,0,1,2,3,4,5
print(line_break)
"""This is fairly easy to understand. In each call, the value of the number variable is printed. 
We then check whether the base case has been fulfilled. 
If not, we make a recursive call to the function with the current value decremented.

One thing to notice is that an outer call cannot move forward until all the inner recursive calls 
have finished. This is why we get a sequence of 5 to 0 to 5 printed."""
#creating a factorial recursive function
def factorial(n):
    if n == 0 or n == 1: #base cases (if input is 1, 0, or negative, this function stops)
        return 1
    if n < 0:
        return -1
    return n * factorial(n-1) #recursive function repeats til base case above is completed
print(factorial(5))
print(factorial(9))
















