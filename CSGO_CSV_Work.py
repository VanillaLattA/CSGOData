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


def averageBSPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        battlescarredSkinPrice = 0
        columnLength = 0
        for row in csv_dict_reader:
            if(row['BattleScarred']=='NA'):
                pass
            else:
                battlescarredSkinPrice +=float(row['BattleScarred'])
                columnLength +=1
        return battlescarredSkinPrice/columnLength
averageBSPrice() 

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
        return wellwornSkinPrice/columnLength
averageWWPrice() 

def averageFTPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageFTSkinPrice= 0
        columnLength= 0
        for row in csv_dict_reader:
            if(row['Field-Tested']=='NA'):
                pass
            else:
                averageFTSkinPrice += float(row['Field-Tested'])
                columnLength += 1
        return averageFTSkinPrice
averageFTPrice()

def averageMWPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageMWSkinPrice= 0
        columnLength= 0
        for row in csv_dict_reader:
            if(row['Minimal-Wear']== 'NA'):
                pass
            else:
                averageMWSkinPrice += float(row['Minimal-Wear'])
                columnLength += 1
        return averageMWSkinPrice
averageMWPrice()

def averageFNPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageFNSkinPrice= 0
        columnLength= 0
        for row in csv_dict_reader:
            if(row['Factory-New']== 'NA'):
                pass
            else:
                averageFNSkinPrice  += float(row['Factory-New'])
                columnLength += 1
        return averageFNSkinPrice
averageFNPrice()

def averageSTBSPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageSTBSSkinPrice= 0
        columnLength= 0
        for row in csv_dict_reader:
            if(row['ST-Battle-Scarred']== 'NA'):
                pass
            else:
                averageSTBSSkinPrice += float(row['ST-Battle-Scarred'])
                columnLength +=1
        return averageSTBSSkinPrice
averageSTBSPrice()

def averageSTWWPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageSTWWSkinPrice= 0
        columnLength= 0
        for row in csv_dict_reader:
            if(row['ST-Well-Worn']=='NA'):
                pass
            else:
                averageSTWWSkinPrice += float(row['ST-Well-Worn'])
                columnLength += 1
        return averageSTWWSkinPrice
averageSTWWPrice()

                
def averageSTFTPrice(): #These are todo
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageSTFTSkinPrice = 0
        columnLength = 0
        for row in csv_dict_reader:
            if(row['ST-Field-Tested']== 'NA'):
                pass
            else:
                averageSTFTSkinPrice+= float(row['ST-Field-Tested'])
                columnLength+=1      
        return averageSTFTSkinPrice

def averageSTMWPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageSTMWPrice = 0
        columnLength= 0
        for row in csv_dict_reader:
            if(row['ST-Minimal-Wear']=='NA'):
                pass
            else:
                averageSTMWPrice += float(row['ST-Minimal-Wear'])
                columnLength+= 1
    return averageSTMWPrice
averageSTMWPrice()                

def averageSTFNPrice():
    with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
        csv_dict_reader = DictReader(read_obj)
        averageSTFNPrice= 0
        columnLength = 0
        for row in csv_dict_reader:
            if(row['ST-Factory-New']== 'NA'):
                pass
            else:
                averageSTFNPrice+= float(row['ST-Factory-New'])
                columnLength+= 1
        return averageSTFNPrice
    
averageSTFNPrice()

#TODO: Function that compares average from one condition to the next, what is the greatest condition jump
#TODO: Plot the greatest increase in AK prices based on condition. Make sure that the return statements are 
#working well and that all the data can fit in 1 jupyter notebook.

def printAvgPrices(): #this will replace all the pring statements 
    battlescarred= averageBSPrice()
    print(battlescarred)
    wellworn = averageWWPrice()
    print(wellworn)
    fieldtested = averageFTPrice()
    print(fieldtested)
    minimalwear = averageMWPrice()
    print(minimalwear)
    factorynew= averageFNPrice()
    print(factorynew)
    stbattlescarred= averageSTBSPrice()
    print(stbattlescarred)
    stwellworn =averageSTWWPrice()
    print(stwellworn)
    stfieldtested= averageSTFTPrice()
    print(stfieldtested)
    stminimalwear= averageSTMWPrice()
    print(stminimalwear)
    stfactorynew= averageSTFNPrice()
    print(stfactorynew)
    
printAvgPrices()
