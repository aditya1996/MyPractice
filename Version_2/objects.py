import sqlite3

class MyWarehouse():


    def __init__(self,wname,oname,loc,capacity):

        self.wname = wname
        self.oname = oname
        self.loc = loc
        self.capacity = capacity
        print(f"\nYour warehouse by the name of {oname} has been created\n")

    def __str__(self):

        return f'{self.wname} warehouse is owned by {self.oname} located in {self.loc}'+'\n'+f'It has a capacity of {self.capacity} cars'

    def add_car(self,name,brand,kms,mil):

        conn = sqlite3.connect('cars.db')
        print("\nDatabase accessed!\n")

        c = conn.cursor()

        try:
            c.execute("""CREATE TABLE Cars (                            
                Name text,
                Brand text,
                KmsDone integer,
                Mileage integer
                )""")
            print("\nCars Table Created!!\n")
        except:
            print("\nCars Table Found\n")

        with conn:
            c.execute("INSERT INTO cars VALUES (:Name,:Brand,:KmsDone,:Mileage)", {'Name': name,'Brand': brand, 'KmsDone': kms, 'Mileage': mil})

        print("\nCurrent Database is: \n")
        c.execute(" SELECT * FROM cars")
        print(c.fetchall())
        

    def view_car(self):

        conn = sqlite3.connect('cars.db')
        print("\nDatabase accessed!!\n")

        c = conn.cursor()

        c.execute(" SELECT * FROM cars")
        print(c.fetchall())


    def update_mil(self,name,value):

        conn = sqlite3.connect('cars.db')
        print("\nDatabase accessed!!\n")

        c = conn.cursor()

        with conn:
            c.execute("""UPDATE Cars SET Mileage = :Mileage
                        WHERE Name = :Name""",
                    {'Mileage': value, 'Name': name})


    def best_mileage(self):

        conn = sqlite3.connect('cars.db')
        print("\nDatabase accessed!!\n")

        c = conn.cursor()

        c.execute(" SELECT * FROM cars")
        
        l = list(c.fetchall())
        c = []

        for i in l:
            c.append(i[3])

        max_mil = max(c)

        for n in l:

            if n[3] == max_mil:
                print(f"\nThe car having most mileage is {n[0]} by {n[1]}\n")


    def remove_car(self,name):

        conn = sqlite3.connect('cars.db')
        print("\nDatabase accessed!!\n")

        c = conn.cursor()

        with conn:
            c.execute("DELETE from Cars WHERE Name = :Name",{'Name': name})

        print(f'\n{name} has been deleted from your database\n')