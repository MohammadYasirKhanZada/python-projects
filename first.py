### Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input('Enter your name:') #getting user name
age = int(input('Enter your age:')) # getting user input
year = str((2020 - age) + 100) #converting into string 
print(name + 'will be 100 years old in the year of: ' + year)  # final output
