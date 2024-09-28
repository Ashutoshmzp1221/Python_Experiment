import linear_method, cubic_spline

print("--------Ashutosh Dwivedi---------")
print("-----------21BCS2617-------------")
choice = 'p'

while(choice != '3'):
    print("Enter the choice: ")
    print("Enter 1 for linear method")
    print("Enter 2 for cubic method")
    print("Enter 3 to exit ")
    choice = input()

    if choice == '1':
        linear_method.plot_the_graph()
    elif choice == '2':
        cubic_spline.plot_the_graph()
    elif choice == '3':
        print("Exiting the program")
    else:
        print("Invalid choice!")