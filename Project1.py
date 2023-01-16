# Project Details
# CRUD operation {CREATE, RETRIEVE, UPDATE, DELETE}

"""
    Inventory Management Client using python
    Item Colums
        1. itemId
        2. itemName
        3. quantity
"""
import csv
class InventoryManagement():
    def __init__(self) -> None:
        pass
    
    def __init__(self, username):
        self.username = username
        print("Welcome", username)
    
    @classmethod
    def insertItem(cls, itemId, itemName, quantity):
        cls.itemId = itemId
        cls.itemName = itemName
        cls.quantity = quantity

        try:
            dbFile = open("data/ItemMaster.csv", 'a')
            dbFileRead = dbFile.read()
            # print(dbFileRead)
            # dbFile.close()

            # Logic to check if item already exists in the file
            if cls.itemId in dbFileRead:
                print("Item already exists.")
            else:
                dbFile.write(cls.itemId + ',' + cls.itemName + ',' + cls.quantity + "\n")
        except:
            print("File doesn't exits")
    @classmethod
    def displayItem(cls, itemId):
        dbFile = open("data/ItemMaster.csv", 'r')
        items = dbFile.read()

        if itemId in items:
            print(itemId.readline())
        else:
            print("Item doen't exists")
        dbFile.close()

    def __del__(self):
        pass



iv = InventoryManagement

ans = 'y'
while ans != 'x':
    ans = input("Please enter your choice (C/U/R/D/X/)").lower()
    if ans == 'r':
        itemId = input("Enter Item ID: ")
        iv.displayItem(itemId)
    elif ans == 'c':
        itemId = input("Enter itemId: ")
        itemName = input("Enter the name of the item: ")
        quantity = input("Enter the quantity of the item: ")
        iv.insertItem(itemId, itemName, quantity)
    # elif ans == 'u':

    # elif ans == 'd':


    # else:
    #     print("Invalid!")

iv.displayItem("1")

        