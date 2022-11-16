## Practice chapter 1:
# 1.Guess result of expression without executing it:

# a) 1 <= 1   True 

# b) 1 != 1   False

# c) 1 != 2   True

# 2. Make all of them true.
    
# a) 3 __ 4

print(3 != 4)

# b) 10 __ 5

print(10 > 5)

# c) 42 __ "42"

print(42 >= 42)


## Practice chapter 2
# 1. Print the text in which there will be a quote with double quotes.

print('Something text in quotes: "Hey, have a nice day!" ')

# 2. Print the text in which there will be an apostrophe.

print("Hey, here you can see the word with apostrophe: м'ята ")

# 3. Print one line that will be displayed on several lines
print("""This text will be divided into several parts.
 Some another text.""")

# 4. Print text that doesn`t fit in one line but will be displayed in one line.
print("This text will be divided into several parts \
Some another text.\
")

## Practice chapter 3
# 1. Create a variable with data type string. Count the length of this line.
first_string = 'My name is Yaroslava.'
print('Length of the string:', len(first_string))

# 2. Create another variable with string data type. Output the result of concatenation of these two variables.
second_string = "I'm 20 years old."
print('Concatenation of two variables: ', first_string + second_string)

# 3. Print the two previous variables, but with a space between them.
print('Concatenation of two variables with space: ', first_string + ' ' + second_string)

# 4. Get a string from user input. Check if the string is a palindrome.
string_input = input('Enter some sentence:')
if(string_input==string_input[::-1]):
      print(f"The string ['{string_input}'] is a palindrome")
else:
      print(f"The string ['{string_input}'] is not a palindrome")

# 5. Replace age in the following string with your age. `"I'm 10 years old" -> "I'm 30 years old"`. Do it with:
# a) indexing
age = '20'
string_a_task = "I'm 10 years old."
new_string = string_a_task[:4] + age + string_a_task[6:]
print(new_string)

# b) replace function. 

string_b_task = "I'm 10 years old."
print(string_b_task.replace('10', '20'))


## Practice chapter 4

# 1. The program receive user's name and age from input. Then you need to display the name and age in one line in several ways:

input_name = input("Enter your name:")
input_age = int(input("Enter your age:"))

# a) by listing all the parameters in the print function
print("Your name is", input_name, "and you are", input_age, "years old.")

# b) by formatting a string using the format function
person_info = "Your name is {name} and you are {age} years old."
print(person_info.format(name=input_name, age=input_age))

# c) by formatting a string with f-string
print(f"Your name is {input_name} and you are {input_age} years old.")


## Practice chapter 5
# Format string with a proper functions

# 1. All letters must be written in lowercase.

string_1 = "Animals  "
print(string_1.lower())
# 2. All letters must be capitalized.

string_2 = "  Badger"
print(string_2.upper())

# 3. Remove all spaces:

string_3 = "   HoneyPot   "

#    a) from the beginning of the line
print("Remove all spaces from the beginning of the line:", string_3.lstrip())

#    b) from the end of the line
print("Remove all spaces from the end of the line:", string_3.rstrip())

#    c) on both sides of the line

print("Remove all spaces from both sides of the line:", string_3.strip())

# 4. Check the value of the startwith ('Be') function for each line.:

string1 = "Bear"
string2 = "bear"
string3 = "BEAR"
string4 = "bEar"
string_1_check, string_2_check, string_3_check, string_4_check = string1.startswith("Be"), string2.startswith("Be"), \
    string3.startswith("Be"), string4.startswith("Be")
print(string_1_check, string_2_check, string_3_check, string_4_check)


# Convert rows with methods from prev exercise to have positive result for each row.
# string2 = "bear"
string2 = string2.capitalize()

# string3 = "BEAR" and string4 = "bEar"
string3, string4 = string3.lower(), string4.lower()
string3, string4 = string3.capitalize(), string4.capitalize()

string1_check, string2_check, string3_check, string4_check = string1.startswith("Be"), string2.startswith("Be"), \
    string3.startswith("Be"), string4.startswith("Be")
print(string1_check, string2_check, string3_check, string4_check)

# 5. Find and replace all letters 's' with the letter 'x' in the following line: 

some_string = "Somebody said something to Samantha."
some_string = some_string.replace('s', 'x')
some_string = some_string.replace('S', 'x')
print(some_string)


# 6. Leave only numbers in the following line using only string methods: 
symbols_string = '12345!,_6--'
only_digit_string = symbols_string[:5] + symbols_string[8]
print(only_digit_string)

# only_digit_string = ''.join(element for element in symbols_string if element.isdigit())




    
