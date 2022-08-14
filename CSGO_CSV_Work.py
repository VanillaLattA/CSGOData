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
#printTypeAndSkin() uncomment when needed to print

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

#TODO: Function for all other conditions
#TODO: Function that compares average from one condition to the next, what is the greatest condition jump
#TODO: Plot the greatest increase in AK prices based on condition. Make sure that the return statements are 
#working well and that all the data can fit in 1 jupyter notebook.

def averageWWPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        wellwornSkinPrice=0
        columnLength=0 
        for row in csv_dict_reader:
            if(row['Well-Worn']=='NA'):
                pass
            else:
                wellwornSkinPrice += float(row['Well-Worn'])
                columnLength+=1
        print('Average well-worn price is: ' + str(wellwornSkinPrice/columnLength))
averageWWPrice() #Nice it works
