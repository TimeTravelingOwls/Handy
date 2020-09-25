# A few handy functions

# Converts input to lower case, splits words into a list
def get_smart(prompt):
  raw_input = input(prompt)
  # Convert the input to lower case:
  smooth_input = raw_input.lower()
  # Convert the lower case input into a list:
  input_list = smooth_input.split()
#  print(input_list) # for testing
  return(input_list)

# Checks whether *name* appears in *list*
def is_in(name, list):
  if name in list:
    return(True)
  else:
    return(False)

# Sample functions
def eat(fruit):
  print('OK, you ate the', fruit)

def take(fruit):
  print('OK, you took the', fruit)

def peel(fruit):
  print('OK, you peeled the', fruit)

def throw(fruit):
  print('OK, you threw the', fruit)

# Example - first, a familiar list, then a new one:
fruit = ['apples', 'oranges', 'pears', 'bananas']
commands = ['take', 'peel', 'throw', 'eat']

# Get user input, e.g., take apples
user_command = get_smart("Enter a command: ")

# Check command - *False* if the command is valid
if not is_in(user_command[0], commands):
  print(user_command[0], 'is a not a command I recognize')
  print('I know these commands: ', commands)

# Check fruit - *False* if the fruit is valid
elif not is_in(user_command[1], fruit):
  print(user_command[1], 'is a not a fruit I recognize')
  print('I know these fruits: ', fruit)  

# If they're both *False,* then  
else:  
  print('\n->', *user_command, '<- is legit!\n')
# FYI, this is pure magic:
  globals()[user_command[0]](user_command[1])
