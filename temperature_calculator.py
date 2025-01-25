# Write a program that continuously prompts the user for a 
# temperture (in the scale of your choosing). Every time 
# the user inputs a temperature, the program should report 
# the mean of all the values entered so far. When the user
# types in 'quit' the program should terminate.
#
# An example interaction might look like
# Input a temperature
# >> 42
# The average temperature so far is 42
# Input a temperature
# >> 26
# The average temperature so far is 34.0
# Input a temperature
# >> 52
# The average temperature so far is 40.0
# >> quit
# Goodbye
#
# You can use the sum function to sum all the values in a list
# sum(<list>)

def temperature_calculator():
    
    temp_list = []
    raw_value = input('Please input a temperature: ')
    value = raw_value.lower()
    while True:
        if value != 'quit':
            float_value = float(value)
            temp_list.append(float_value)
            temp_list_average = sum(temp_list) / len(temp_list)
            raw_value = input(f'Your average temperature is {temp_list_average}. Please input another temperature or type "Quit" if you are done: ')
            value = raw_value.lower()
        else:
            print('Goodbye.')
            break

        




if __name__ == "__main__":
    temperature_calculator()