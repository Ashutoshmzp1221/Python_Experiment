import bisection_methode, newton

print("-----------------WELCOME---------------------")
print("Ashutosh Dwivedi--------------------21BCS2617\n")

choice = 'p'

while True:
    print("Select your choice")
    print("Enter 1 for the bisection methode.")
    print("Enter 2 for the newton raphason methode")
    print("Else exit")
    choice = input("Now enter your choice: ")
    if choice == '1':
        bisection_methode.main()
        print("\n")
    elif choice == '2':
        newton.main()
        print("\n")
    else:
        print("Tata bye bye! Have great day")
        break
