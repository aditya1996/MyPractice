from objects import MyWarehouse

def program():

    # owner = input("Please enter your name!!\n")
    # your_warehouse = input("Please enter the name of your Warehouse!!\n")
    # your_location = input("Please enter the location of your Warehouse!!\n")
    # your_capacity = int(input("Please enter the capacity of your Warehouse!!\n"))

    ware = MyWarehouse('Ferrari Cars','Aditya','Lucknow',50)

    while True:
        print("Your warehouse {} is up and running!! Owned by {} and having capacity of {} cars".format(ware.wname,ware.oname,ware.capacity))
        print("1. Enter 'S' to create SQLite3 DB from Excel File")
        print("2. Enter 'C' to loads the cars from sql data to Pandas Dataframe")
        print("3. Enter 'D' to see how many cars are present from each manufacturer")
        print("4. Enter 'X' to exit  this program")


        inpi = input("Please enter your choice: \n")

        if inpi[0].lower() == 's':

            ware.create_sqldb_from_excel()

        elif inpi[0].lower() == 'c':

            ware.load_db()

        elif inpi[0].lower() == 'd':

            ware.num_make()

        elif inpi[0].lower() == 'x':
            print("You have quit the Warehouse Operations\n...loading main menu...\n")
            break