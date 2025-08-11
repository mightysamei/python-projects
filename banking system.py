accounts = {}
print("Welcome to Simple Bank!")

while True:
    print("\nWhat would you like to do?")
    print("1. Check balance")
    print("2. Create account")
    print("3. Add money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        num = input("Enter account number: ").strip()
        if num in accounts:
            print(f"Balance: Rs{accounts[num]}")
        else:
            print("❌ Account not found")
    
    elif choice == "2":
        num = input("Enter new account number: ").strip()
        if num in accounts:
            print("⚠️ Account already exists!")
        else:
            accounts[num] = 0
            print(f"✅ Account {num} created with Rs0")
    
    elif choice == "3":
        num = input("Enter account number: ").strip()
        if num in accounts:
            try:
                money = int(input("Enter amount to add: Rs").strip())
                if money > 0:
                    accounts[num] += money
                    print(f"✅ Added Rs{money}. New balance: Rs{accounts[num]}")
                else:
                    print("⚠️ Amount must be positive")
            except ValueError:
                print("❌ Please enter a valid number")
        else:
            print("❌ Account not found")
    
    elif choice == "4":
        print("🏦 Thank you for banking with us!")
        break
    
    else:
        print("⚠️ Please enter 1, 2, 3 or 4")
