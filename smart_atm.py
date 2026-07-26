current_balance = 500.00 

withdraw = float(input("Enter amount to withdraw: R"))

if withdraw > 0: 
    if withdraw <= current_balance:
        current_balance -= withdraw
        print(f"Withdrawal successful! Remaining balance amount: R{current_balance}")
    else:
        print("Declined. Insufficient funds.")
elif withdraw <= 0:
    print("Invalid amount. You must withdraw more than R0.00.")