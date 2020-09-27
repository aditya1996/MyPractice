from objects import MyWarehouse

def program():

    # owner = input("Please enter your name!!\n")
    # your_warehouse = input("Please enter the name of your Warehouse!!\n")
    # your_location = input("Please enter the location of your Warehouse!!\n")
    # your_capacity = int(input("Please enter the capacity of your Warehouse!!\n"))

    ware = MyWarehouse('Ferrari Cars','Aditya','Lucknow',50)

    while True:
        print(f"Your warehouse {ware.wname} is up and running!! Owned by {ware.oname} and having capacity of {ware.capacity} cars")
        print("1. Enter 'A' to add a car")
        print("2. Enter 'U' to update a car's mileage")
        print("3. Enter 'S' to see your cars")
        print("4. Enter 'R' to remove a Car from your Warehouse")
        print("5. Enter 'B' to see which car has best mileage")
        print("6. Enter 'X' to exit this Warehouse\n")

        inpi = input("Please enter your choice: \n")

        if inpi[0].lower() == 'a':

            n = input("\nPlease enter the name of the car \n")
            b = input("Please enter the brand of the car \n")
            kms = int(input("Please enter the number of kms done \n"))
            mil = int(input("Please enter the mileage of this car \n"))
            ware.add_car(n,b,kms,mil)
            print(f"\nYour car {n} by {b} has been added to the Warehouse\n")

        elif inpi[0].lower() == 's':

            ware.view_car()

        elif inpi[0].lower() == 'u':

            name = input("Please enter the name of the car you want to update: \n")
            value = input("Which value do you want us to put ?")
            
            ware.update_mil(name,value)

        elif inpi[0].lower() == 'b':
             ware.best_mileage()
            
        elif inpi[0].lower() == 'r':
            car_remove = input("Please provide the name of the car you want to remove: \n")
            ware.remove_car(car_remove)

        elif inpi[0].lower() == 'x':
            print("You have quit the Warehouse Operations\n...loading main menu...\n")
            break