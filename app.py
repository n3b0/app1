#birth_year = input('Birth year: ')
#age = 2021 - int(birth_year)
#print(age)


#name = input("What is your name?" )
#if name : 'Ian'
#print("I love you Iggy Buggy!!!" )
#if name : 'Nea'
#print('Wow you are so sexy..')

#course = 'Python for beginners'
#another = course[:]
#print(another)

#name = 'Jennifer'
#print(name[1:-1])

#first = 'John'
#last = 'Smith'
#message = first + ' [' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(msg)
#John [Smith] is a coder

#course = 'Python for beginners'
#print(len(course))
#print(course.lower())
#print(course.replace('P' , 'G'))
#print('python' in course)

#Arithmetic Operations
#print(10 ** 3)
#x = 10
#x += 3
#x = x + 3
#x += 3
#print(x)
# didn't work?

# Operator precedence
#x = (10 + 3) * 2 ** 2
#print(x)

#x = 2.9
#print(round(x))
#print(abs(-2.9)) #makes it positive
 

#course = 'Python for Beginners' 
#another = course[:]
#print(another)

#name = 'Jennifer'
#print(name[1:-1])

#first = 'John'
#last = 'Smith'
#message = first + ' [' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(msg)
#John [Smith] is a coder

#course = 'Python for Beginners'
#print(len(course))
#print(course.upper()) #method-OOP bc it belongs
#print(course.lower())
#print(course)
#print(course.replace('P', 'J'))
#print('python' in course) #in --> boolean value: true/false 

#Arithmetic Operations
#10- integers, 10.123 - floats
#print(10 ** 3)
#x = 10
#x = x + 3
#x -= 3
#print(x)

#Operator Precedence: (),**, *, +
#x = (10 + 3) * 2 ** 2
#print(x)

#Math Functions
#import math
#print(math.floor(2.9))
#x = 2.9
#print(round(x))
#print(abs(-2.9))

#If Statements
#is_hot = False
#is_cold = False

#if is_hot:
    #print("It's a hot day")
    #print("Drink plenty of water")
#elif is_cold:
    #print("It's a cold day")
    #print("Wear warm clothes")
#else: 
    #print("It's a lovely day")

#print("Enjoy your day")

#price = 1000000
#has_good_credit = True
#if has_good_credit:
    #down_payment = 0.1 * price
#else:
    #down_payment = 0.2 * price
#print(f"Down payment: ${down_payment}")

#Logical Operators - multiple conditions (and)
#AND: both
#OR: at least one
#NOT: and not - 1 is true and another is false, converts both to false
#has_high_income = False
#has_good_credit = True
#has_criminal_record = True

#if has_good_credit and has_high_income:
    #print("Eligible for loan")

#if has_good_credit or has_high_income:
    #print("Eligible for loan")

#if has_good_credit and not has_criminal_record:
    #print("Eligible for loan")
#example is kind of in bad taste....

#Comparison Operators : comparing variable with a value, <,>,<=, >=, ==, !=(not equal)

#temperature = 35

#if temperature > 30:
    #print("It's a hot day")
#else:
    #print("It's not a hot day")

#name = "John"
#if len(name) < 3:
    #print("Name must be at least 3 characters")
#elif len(name) > 50:
    #print("Name can be a maximum of 50 characters")

#else :
    #print("Name looks good!")

#Weight Converter Project .......
#weight = int(input('Weight: '))
#unit = input(' (L)bs or (K)g: ')
#if unit.upper() == "L" :
    #converted = weight * 0.45
    #print(f"You are {converted} kilos")
#else:
    #converted = weight / 0.45
    #print(f"You are {converted} pounds")

#While loops
#i = 1       
#while i <= 5:
    #print('*' * i)
    #i = i + 1
#print("Done")

#Guessing Game
#secret_number = 9
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
    #guess = int(input('Guess: '))
    #guess_count += 1
    #if guess == secret_number:
        #print("You won!")
        #break
#else:
    #print('Sorry, you failed')    

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number   
print(max)                

