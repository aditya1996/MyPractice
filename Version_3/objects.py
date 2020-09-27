import sqlite3
import pandas as pd
import pickle
from matplotlib import pyplot as plt

class MyWarehouse():


    def __init__(self,wname,oname,loc,capacity):

        self.wname = wname
        self.oname = oname
        self.loc = loc
        self.capacity = capacity
        print("\nYour warehouse by the name of {} has been created\n".format(oname))

    # This function creates SQLite3 DB from Excel File

    def create_sqldb_from_excel(self):

        data = pd.read_csv('/Users/adityatiwari/Desktop/Python/CarWarehouse/Version_3/excel_data/car_data.csv')

        car_list = data[['make','fuel-type', 'aspiration','num-of-doors','body-style',
        'drive-wheels','engine-location','horsepower','city-mpg','highway-mpg','price']]

        conn = sqlite3.connect('/Users/adityatiwari/Desktop/Python/CarWarehouse/Version_3/database/cars.db')
        print("\nDatabase accessed!\n")

        car_list.to_sql('Cars', conn, if_exists='replace', index=False)

        print("Database has been created from excel\n")
        conn.commit()
        conn.close()

    # This function loads the cars from sql data to Pandas Dataframe. This Dataframe is stored by pickle.

    def load_db(self):

        conn = sqlite3.connect('/Users/adityatiwari/Desktop/Python/CarWarehouse/Version_3/database/cars.db')

        sql_query = pd.read_sql_query(''' Select * from  Cars''',conn)

        df = pd.DataFrame(sql_query, columns=['make','fuel-type', 'aspiration','num-of-doors','body-style',
        'drive-wheels','engine-location','horsepower','city-mpg','highway-mpg','price'])
		
        print("\n\nA DataFrame has been created from your Cars Table in SQL DB.\nHere is a Short Glimpse...")
        print(df.head())

        df.to_pickle('/Users/adityatiwari/Desktop/Python/CarWarehouse/Version_3/DataFrame/Car_DataFrame')

    def num_make(self):

        df = pd.read_pickle('/Users/adityatiwari/Desktop/Python/CarWarehouse/Version_3/DataFrame/Car_DataFrame')

        print(df['make'].value_counts())

        car_manf = []
        no_cars = []

        car_cnt = df['make'].value_counts().to_dict()

        for key,value in car_cnt.items():
            car_manf.append(key)
            no_cars.append(value)

        # Plotting Bar Chart

        plt.style.use('fivethirtyeight')
        
        plt.bar(car_manf[:6],no_cars[:6])

        plt.title('No. of cars from each manufacturer')
        plt.xlabel('Manufacturer')
        plt.ylabel('No. of Cars')

        plt.show()


	


