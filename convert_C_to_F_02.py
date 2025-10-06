# FILE NAME - convert_C_to_F_02.py

# NAME: kevin hormaza
# DATE: October 6, 2025
# BRIEF DESCRIPTION: This program converts temperatures between Celsius and Fahrenheit.
# The user chooses which conversion to perform and enters a temperature.
# The program then displays the converted value.


# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====\n")
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius\n")

choice = int(input("Please choose from the above menu: "))
temperature = float(input("Enter a temperature to convert: "))

if choice == 1:
    result = temperature * 9/5 + 32
    print(f"\n{temperature} degrees Celsius is {result} degrees Fahrenheit.")
elif choice == 2:
    result = (temperature - 32) * 5/9
    print(f"\n{temperature} degrees Fahrenheit is {result} degrees Celsius.")




########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
That small changes in formulas can make a big difference in output.
I already used if and elif in a previous project, but this lab helped me apply them in a cleaner way.
It showed how small changes in math formulas can completely change the output, 
so I learned to double check parentheses and arithmetic first.






'''
