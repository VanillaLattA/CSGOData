import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from csv import DictReader


# Python program to read CSV file line by line
# import necessary packages
import csv
  
# Open file 
with open('CSGOskinsCSV.csv', 'r') as read_obj:   
    csv_dict_reader = DictReader(read_obj)
    #column_names = csv_dict_reader.fieldnames      This reads all the column names
    
    def printTypeAndSkin():
        for row in csv_dict_reader:
            print(row['Type'],row['Skin'])
    def average_BS_skinPrice():
        battlescarredSkinPrice= 0
        for row in csv_dict_reader:
            if(row['BattleScarred']=='NA'):
                pass
            else:
                battlescarredSkinPrice += float(row['BattleScarred'])
        print(battlescarredSkinPrice)
    average_BS_skinPrice()
