import pickle
import sqlite3
from menu import program

if __name__ == "__main__":

    while True:
        print("\n\nWelcome to this WareHouse Routing System! \nWould you like to create your own Warehouse ?\n")
        inp = input("Enter 'y' to make a Warehouse or 'n' to exit this program\n")
        
        if inp[0].lower() == 'y':
            program()
        elif inp[0].lower() == 'n':
            print("\nExiting Program...\n")
            break
        else:
            print("\nSry I did not understand that! Please enter a valid choice...\n")
