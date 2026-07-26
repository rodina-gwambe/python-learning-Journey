# Acountdown using while loop

count = 5

while count > 0:
    print(count)
    count = count - 1
print("Countdown complete!")

#Building a simple rep counter for the gym with a for loop.Python handles the math here no need to add it
for rep in range(1, 11): #rep 11 wont be printed as the range function stops at 10
    print(f"Rep {rep} complete!")   

