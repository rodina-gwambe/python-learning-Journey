kilometers = (float(input("Enter the distance in kilometers: ")))
petrol_price = (float(input("Enter the price of fuel per liter: ")))
liters_needed = round(kilometers / 10, 2)   #Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
fuel_cost = round(liters_needed * petrol_price, 2)

print(f'The distance of {kilometers} kilometers will require {liters_needed} liters of fuel.')
print(f'The total fuel cost for the trip will be R{fuel_cost}')  
  