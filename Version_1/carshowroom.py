import pickle

class MyWarehouse():

    allowedtype = "4 Wheelers"

    def __init__(self,name,sname,loc,capacity,carls=[],no=1):

        self.name = name
        self.sname = sname
        self.loc = loc
        self.capacity = capacity
        self.carls = carls
        self.no = no
        print(f"Your warehouse by the name of {sname} has been created")

    def __str__(self):

        return f'{self.sname} warehouse is owned by {self.name} located in {self.loc}'+'\n'+f'It has a capacity of {self.capacity} cars and currently we have {len(self.carls)} cars'+'\n'+ str(self.carls)

    def addcar(self,name,brand,kmsdone,mileage):

        self.carls.append([name,brand,kmsdone,mileage])

        with open('carlist.data', 'wb') as filehandle:
            pickle.dump(self.carls, filehandle)   # store the data as binary data stream
        print(f'{name} has been added to the Showroom.')

    def removecar(self,name):

        l = len(self.carls)

        carls_test = []

        with open('carlist.data', 'rb') as filehandle:
            carls_test = pickle.load(filehandle)

        try:
            for i in range(0,l):
                for j in range(0,5):
                    if carls_test[i][j] == name:
                        carls_test.pop(i)
        except IndexError:
            pass

        with open('carlist.data', 'wb') as filehandle:
            pickle.dump(carls_test, filehandle)

        try:
            for i in range(0,l):
                for j in range(0,5):
                    if self.carls[i][j] == name:
                        self.carls.pop(i)
        except IndexError:
            pass

        with open('carlist.data', 'wb') as filehandle:
            pickle.dump(carls_test, filehandle)

        print(f'Your car {name} has been removed from the {self.sname} Warehouse')



    def bestmileage(self):

        list = []
        l = len(self.carls)

        for i in range(0,l):
                list.append(self.carls[i][3])

        for i in range(0,l):
                    if self.carls[i][3] == max(list):
                        print(f'The car having best mileage is {self.carls[i][0]} with mileage of {max(list)} km/l')
    
    def loadcars(self):

        with open('carlist.data', 'rb') as filehandle:
            self.carls = pickle.load(filehandle) # read the data as binary data stream

        print(f'The list of cars have been loaded! and below is your collection:')
        print(self.carls)

def program():

    nwahr = input("Please enter your name!!\n")
    snwahr = input("Please enter the name of your Warehouse!!\n")
    lwahr = input("Please enter the location of your Warehouse!!\n")
    cwahr = int(input("Please enter the capacity of your Warehouse!!\n"))

    ware = MyWarehouse(nwahr,snwahr,lwahr,cwahr)

    while True:
        print(f"Your warehouse {ware.sname} is up and running!! Owned by {ware.name} and having capacity of {ware.capacity} cars\n")
        print("1. Enter 'A' to add a car")
        print("2. Enter 'L' to load previous cars")
        print("3. Enter 'P' to preview your current Warehouse")
        print("3. Enter 'S' to see your cars")
        print("4. Enter 'R' to remove a Car from your Warehouse")
        print("5. Enter 'B' to see which car has best mileage")
        print("6. Enter 'X' to exit this Warehouse\n")

        inpi = input("Please enter your choice: \n")

        if inpi[0].lower() == 'a':

            n = input("Please enter the name of the car \n")
            b = input("Please enter the brand of the car \n")
            kms = int(input("Please enter the number of kms done \n"))
            mil = int(input("Please enter the mileage of this car \n"))
            ware.addcar(n,b,kms,mil)
            print(f"Your car {n} by {b} has been added to the Warehouse")

        elif inpi[0].lower() == 's':

            print("\nHere is a list of cars you own right now!\n")
            for i in range(0,len(ware.carls)):
                print(ware.carls[i])

        elif inpi[0].lower() == 'l':

            ware.loadcars()

        elif inpi[0].lower() == 'b':
            ware.bestmileage()
            
        elif inpi[0].lower() == 'r':
            car_remove = input("Please provide the name of the car you want to remove: \n")
            ware.removecar(car_remove)

        elif inpi[0].lower() == 'x':
            print("You have quit the Warehouse Operations\n...loading main menu...\n")
            break


if __name__ == "__main__":

    while True:
        print("Welcome to this WareHouse Routing System! \nWould you like to create your own Warehouse ?\n")
        inp = input("Enter 'y' to make a Warehouse or 'n' to exit this program")
        
        if inp[0].lower() == 'y':
            program()
        elif inp[0].lower() == 'n':
            print("\nExiting Program...\n")
            break
        else:
            print("Sry I did not understand that! Please enter a valid choice...\n")
