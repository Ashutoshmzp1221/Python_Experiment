stack = []
def stack_main():
    print("-------------Stack Operation-------------")
    while True:
        print("Select the operation you want to do: ")
        print("1. For push operation.")
        print("2. For pop operation.")
        print("3. For peek operation.")
        print("4. To print the elements of the stack.")
        print("5. For exiting the program")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            print("Exiting the program.")
            break
        elif choice == 1:
            x = int(input("Enter the number you want to insert: "))
            stack.append(x)
            print(f"Element {x} pushed onto the stack.")
        elif choice == 2:
            print("The poped element is: ",stack.pop())
        elif choice == 3:
            if stack:
                print("The top element is:", stack[-1])
            else:
                print("Stack is empty. No top element.")
        elif choice == 4:
            print("The element of the stack are: ", stack)
        else:
            print("Invalid choice! Please enter a valid choice.")
        print("\n")