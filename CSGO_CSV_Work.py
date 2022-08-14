import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from csv import DictReader
# Python program to read CSV file line by line
# import necessary packages
import csv
#column_names = csv_dict_reader.fieldnames      This reads all the header names



# Open file    
def printTypeAndSkin():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            print(row['Type'],row['Skin'])
    read_obj.close()
printTypeAndSkin()

with open('CSGOskinsCSV.csv', 'r') as read_obj:   
    csv_dict_reader = DictReader(read_obj)
    #column_names = csv_dict_reader.fieldnames      This reads all the column names
    def averageBSPrice():
        battlescarredSkinPrice= 0
        columnLength= 0
        for row in csv_dict_reader:
            if(row['BattleScarred']=='NA'):
                pass
            else:
                battlescarredSkinPrice += float(row['BattleScarred'])
                columnLength += 1
        print('Average battle-scarred price is: ' + str(battlescarredSkinPrice/columnLength)) 
    averageBSPrice()
read_obj.close()
