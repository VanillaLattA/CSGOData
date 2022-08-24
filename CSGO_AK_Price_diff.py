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
        return averageFTSkinPrice/columnLength
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
        return averageMWSkinPrice/columnLength
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
        return averageFNSkinPrice/columnLength
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
        return averageSTBSSkinPrice/columnLength
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
        return averageSTWWSkinPrice/columnLength
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
        return averageSTFTSkinPrice/columnLength

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
    return averageSTMWPrice/columnLength
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
        return averageSTFNPrice/columnLength
    
averageSTFNPrice()

#here let us get the variations from each other of the statistics
battlescarred= averageBSPrice()
wellworn = averageWWPrice()
fieldtested = averageFTPrice() 
minimalwear = averageMWPrice()    
factorynew= averageFNPrice()   
stbattlescarred= averageSTBSPrice()
stwellworn =averageSTWWPrice()    
stfieldtested= averageSTFTPrice()  
stminimalwear= averageSTMWPrice()
stfactorynew= averageSTFNPrice()

def percentageDifference():
    #this function calculates the percentage difference between 
    #each condition and the stat track and non-stattrack
    
    print("The difference between BS and STBS is ", (abs((stbattlescarred-battlescarred)/stbattlescarred)*100),'%')
    print("The difference between WW and STWW is ", (abs((stwellworn-wellworn)/stwellworn)*100),'%')
    print("The difference between FT and STFT is ", (abs((stfieldtested-fieldtested)/stfieldtested)*100),'%')
    print("The difference between MW and STMW is ", (abs((stminimalwear-minimalwear)/stminimalwear)*100),'%')
    print("The difference between FN and STFN is ", (abs((stfactorynew-factorynew)/stfactorynew)*100),'%')
    
    print("From the data we can see that the greatest difference between price is between Field-Tested conditions")
    print("\n")
    #now we need to create the difference between two variants
    prices= [98.00, 133.41, 175.33, 248.25, 368.74, 56.71, 77.53, 88.94, 151.20, 373.75]
    print("The difference between BS and WW is ", abs((wellworn-battlescarred)/wellworn)*100, "%")
    print("The difference between FT and WW is ", abs((fieldtested-wellworn)/fieldtested)*100, "%")
    print("The difference between MW and FT is ", abs((minimalwear-fieldtested)/minimalwear)*100, "%")
    print("The difference between FN and MW is ", abs((factorynew-minimalwear)/factorynew)*100, "%")
    print("\n")
    print("The difference between STBS and STWW is ", abs((stwellworn-stbattlescarred)/stwellworn)*100, "%")
    print("The difference between STFT and STWW is ", abs((stfieldtested-stwellworn)/stfieldtested)*100, "%")
    print("The difference between STMW and STFT is ", abs((stminimalwear-stfieldtested)/stminimalwear)*100, "%")
    print("The difference between STFN and STMW is ", abs((stfactorynew-stminimalwear)/stfactorynew)*100, "%")
percentageDifference()
