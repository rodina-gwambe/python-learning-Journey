num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))

sum=round(num1 + num2, 2)
difference = round(num1 - num2, 2)
product = round(num1 * num2, 2)

if num2 != 0:
    quotient = round(num1 / num2, 2)    
else: 
    quotient = 'undefined (cannot divide by zero)'  

if num2 != 0:
    floor_division = round(num1 // num2, 2)
else:
    floor_division = 'undefined (cannot divide by zero)'

if num2 != 0:
    modulus = round(num1 % num2, 2)
else:
    modulus = 'undefined (cannot divide by zero)'

print(f'The sum of {num1} and {num2} = {sum}')
print(f'The difference of {num1} and {num2} = {difference}')
print(f'The product of {num1} and {num2} = {product}')
print(f'The quotient of {num1} and {num2} = {quotient}')
print(f'The floor division of {num1} and {num2} = {floor_division}')
print(f'The modulus of {num1} and {num2} = {modulus}')