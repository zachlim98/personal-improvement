import pandas as pd 
import matplotlib.pyplot as plt

tfr = pd.read_csv(R"./resources/sweden5.csv") # read file 
tfr["TFR"] = (tfr.drop('Year', axis=1).sum(axis=1)*5)/1000 # sum up TFR


tfr.plot(x='Year',y='TFR')
plt.ylabel("Total Fertility Rate")
plt.title("TFR of Sweden over time") 


weights = [] # create temp list for individual year weights
mac = [] # create list for mean age of childbearing

for z in range(0, len(tfr)): # go through each row
    for i in range(1,(len(tfr.columns)-1)): # then go through each column
        mid = int(tfr.columns[i])+2.5 # calculate the mid-point
        weighted = mid*tfr.iloc[z,i] # calculate the weighted ASFR
        weights.append(weighted) # append it to the temp list
    mac.append((sum(weights)/float(tfr.iloc[z,1:8].sum()))) # sum up the weighted ASFR, divide by sum of ASFR and add to yearly mac list
    weights.clear() # clear the temp list

tfr["MAC"] = mac # add MAC calculation to dataframe


tfr.plot(x="Year", y="MAC")
plt.ylabel("Mean Age of Childbearing")
