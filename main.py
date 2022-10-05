#Write a pseudocode algorithm that prompts the user to enter a three-digit number and outputs the hundreds, tens and units. 
#Example: 523 will output 5 hundreds, 2 tens and 3 units. Use what you learned about division.

number = int(input('Enter a three digit number: '))
hundreds = number%100
tens = (number%100)/10
ones = (number% 100)%10
print(f'{hundreds} hundreds')
print(f'{tens} tens')
print(f'{ones} ones')
