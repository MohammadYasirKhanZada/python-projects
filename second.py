# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

num = int(input('Enter any number:'))
mod = num % 2

if mod == 0:
    print('Oh! you input an even number')
else:
    print("Oh! you have selected a wrong number")