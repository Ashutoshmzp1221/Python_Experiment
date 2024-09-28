age = 21
name = "Ashutosh"
salary = 150000.25
cm_num = 1 + 2j
choice = 'p'

my_details = [age, name, salary, cm_num]
my_details_in_tuple = (age, name, salary, cm_num)
favorite = {
    "favorite_fruit": "mango",
    "favorite_place": "Mirzapur",
    "favorite_food": "Noodles"
}
print("Hello this is practical 1st based on basics of python.")
print("Ashutosh Dwivedi.........21BCS2617\n")
def my_personal_details(choice):
    if choice == '1':
        print(my_details)
        print("\n")
    elif choice == '2':
        print(favorite)
        print("\n")
    elif choice == '3':
        print(my_details_in_tuple)
        print("\n")
    else:
        print("Invalid Choice! Please try again\n")

while choice != '4':
    choice = input("Enter the choice\n1 for details list\n2 for details favorites\n3 for details tuple\n4 exit to quit\n ")
    if choice == '4':
        print("Tata bye bye! If you want any more information hit the run button again")
    else:
        my_personal_details(choice)
