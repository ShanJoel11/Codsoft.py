import random
import string
def generate_passcode(length, include_uppercase=True, include_lowercase=True,
                       include_digits=True, include_symbols=True):
  char = ""
  if include_uppercase:
    char += string.ascii_uppercase
  if include_lowercase:
    char += string.ascii_lowercase
  if include_digits:
    char += string.digits
  if include_symbols:
    char += string.punctuation
  if not char:
    raise ValueError("Atleast one character set must be included (uppercase, lowercase, digits, or symbols)")
  passcode = ''.join(random.choice(char) for _ in range(length))
  return passcode 
while True:
  try:
    length = int(input("Enter passcode length (minimum 8 characters): "))
    if length < 8:
      print("Passcode length must be 8 characters. Please try again.")
    else:
      break
  except ValueError:
    print("Invalid input. Please enter a number.")
include_uppercase = input("Include uppercase letters (u/n)? ").lower() == 'u'
include_lowercase = input("Include lowercase letters (l/n)? ").lower() == 'l'
include_digits = input("Include digits (d/n)? ").lower() == 'd'
include_symbols = input("Include symbols (s/n)? ").lower() == 's'
try:
  passcode = generate_passcode(length, include_uppercase, include_lowercase, include_digits, include_symbols)
  print("Your generated password is:", passcode)
except ValueError as e:
    print(e)
