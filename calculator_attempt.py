'''
Created on Feb 9, 2017

@author: ShermZ
'''
#first attempt at a vacation_calculator forgive my incompetence
def calculate():
    operation = input('''
    please type in the math operation you would like to complete:
    + for addtion
    - for subtraction
    * for multiplication 
    / for division
    ''')
#get la input from user
    number_1 = float(input("enter a number: "))
    number_2 = float(input("enter another number: "))
    print(" ")
#print out what the fuck they are doing on the screen so they can see their stupidity
#a little string formatting for practice and ensuring user sees their numbers
#ADDITION
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2)) #puts the numbers in the string
        print (number_1 + number_2) #prints the answer
#SUBTRACTION
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
#MULTIPLICATION
    elif operation == '*':
        print('{} X {} = '.format(number_1, number_2))
        print(number_1 * number_2)
#DIVISION
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print("invalid input, restart program")
    try_again()
#function to re-enter values without restarting program
def try_again():
    #take input
    again = input(''' 
    Do you wish to use the calculator again?
    type Y for Yes or N for No.
    ''')
    if again.upper() == 'Y':
        calculate()
    elif again.upper() == 'N':
        print("peace mang")
    else:
        try_again()
calculate()
    
    
    
    
    
    
    
    