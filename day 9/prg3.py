balance = 5000
try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise ValueError("Insufficient Balance")
    print("withdrawal successful")
except ValueError as e:
    print("Transaction Failed:",e)                    