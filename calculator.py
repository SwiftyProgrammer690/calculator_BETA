import sys
from sys import exit
user_welcome = input('Hello and welcome to this calculator, please press Y to continue ')

if user_welcome == 'Y' or 'y':
     usr_input_type_selection = str(input('Please tell us how to execute this operation. Division, Multiplication, Addition, or Subtraction?'))
     usr_input_type_selection2 = int(input('Enter the first number'))
     usr_input_type_selection3 = int(input('Enter the second number'))
     if usr_input_type_selection == "Multiplication":
         print("The solution is",usr_input_type_selection2*usr_input_type_selection3)

     elif usr_input_type_selection == "Addition":
         print('The solution is',usr_input_type_selection2+usr_input_type_selection3)

     elif usr_input_type_selection == "Subtraction":
         print('The solution is',usr_input_type_selection2-usr_input_type_selection3)

     elif usr_input_type_selection == "Division":
         print('The solution is ',usr_input_type_selection2/usr_input_type_selection3)

     else:
         sys.exit('Sorry run and try again because this is a invalid answer ERR_NO_OUT')

else:
    sys.exit('That is not a valid answer run and try again :(')
