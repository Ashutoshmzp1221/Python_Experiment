import linked_list,stack,que
choice = 'p'
print("----------------------Welcome----------------------")
while True:
    print("Select your choice: ")
    print("Enter 1 for Linked list.")
    print("Enter 2 for stack.")
    print("Enter 3 for queue.")
    print("Enter 4 to exit")
    choice = input("Enter choice ")
    if(choice == '4'):
        print("Tata bye bye")
        break
    
    elif(choice == '1'):
        print("\n")
        linked_list.linked_main()

    elif(choice == '2'):
        print("\n")
        stack.stack_main()

    elif(choice == '3'):
        print("\n")
        que.que_main()
    
    else:
        print("Invalid choice.")
