#Write a pseudocode algorithm that prompts the user to enter a three-digit number and outputs the hundreds, tens and units. 
#Example: 523 will output 5 hundreds, 2 tens and 3 units. Use what you learned about division.

number = int(input('Enter a three digit number: '))
hundreds = number//100
tens = number//100
ones = number// 100
if hundreds > 0:
  print(f'{hundreds[0]} hundreds')
elif tens > 0:
  print(f'{tens[1]} tens')
elif ones > 0:
  print(f'{ones[2]} ones')
