import pandas as pd 
import matplotlib.pyplot as plt


lifetable = pd.read_csv(R"Resources/sweden3.csv") # import the dataset
lifetable["nqx"] = lifetable["deaths"]/lifetable["survivors"] # prob of dying
lifetable["npx"] = 1 - lifetable["nqx"] # prob of surviving
lifetable.loc[0, "lx"] = 10000 # initial radix 

for i in range(1, len(lifetable)):
    lifetable.loc[i, "lx"] = lifetable.loc[i-1,"npx"] * lifetable.loc[i-1, "lx"] # fill radix columns

for i in range(0, len(lifetable)-1):
    lifetable.loc[i, "ndx"] = lifetable.loc[i, "lx"] - lifetable.loc[i+1, "lx"] # number of people who died in that age group


lifetable["nax"] = 2.5 #set 2.5 for all 5 year intervals
lifetable.loc[0, "nax"] = 0.3 #set 0.3 for the first interval
lifetable.loc[1, "nax"] = 2.0 #set 2.0 for the second interval because it is only a 4 year interval of 1-4

lifetable["n"] = 5 # set the width of the age range to 5
lifetable.loc[0, "n"] = 1 #set 1 for the first interval
lifetable.loc[1, "n"] = 4.0 #set 4.0 for the second interval because it is a 4 year interval of 1-4

for i in range(0, len(lifetable)-1):
    lifetable.loc[i, "nLx"] = (lifetable.loc[i, "nax"]*lifetable.loc[i, "ndx"])  + (lifetable.loc[i+1, "lx"]*lifetable.loc[i,"n"])


lifetable['Tx'] = lifetable.loc[::-1, 'nLx'].cumsum()[::-1] # perform a reverse cumulative sum
lifetable["ex"] = lifetable["Tx"] / lifetable["lx"] # calculate life expectancy at each age group

lifetable.plot(x="age", y="ex")
plt.xlabel("Age")
plt.ylabel("Life Expectancy")
plt.title("Life Expectancy for a cohort")


japan = pd.read_csv(R"Resources/japan4.csv") #import the file
japan["nmx"] = japan["nDx"]/japan["nNx"] #calculate the ASDR or nmx

japan["nqx"] = (japan["n"]*japan["nmx"]/(1+(japan["n"]-japan["nax"])*japan["nmx"])) #perform the Greville-Chiang conversion to find nqx
japan["npx"] = 1-japan["nqx"] #calculate nqx

# from here, it is essentially the same and hence I won't provide more markdown commentary 

japan.loc[0, "lx"] = 10000 # initial radix 

for i in range(1, len(japan)):
    japan.loc[i, "lx"] = japan.loc[i-1,"npx"] * japan.loc[i-1, "lx"] # fill radix columns

for i in range(0, len(japan)-1):
    japan.loc[i, "ndx"] = japan.loc[i, "lx"] - japan.loc[i+1, "lx"] # number of people who died in that age group

for i in range(0, len(japan)-1):
    japan.loc[i, "nLx"] = (japan.loc[i, "nax"]*japan.loc[i, "ndx"])  + (japan.loc[i+1, "lx"]*japan.loc[i,"n"])

japan['Tx'] = japan.loc[::-1, 'nLx'].cumsum()[::-1] # perform a reverse cumulative sum
japan["ex"] = japan["Tx"] / japan["lx"] # calculate life expectancy at each age group

japan.plot(x="Age", y="ex")
plt.xlabel("Age")
plt.ylabel("Life Expectancy")
plt.title("Life Expectancy for Japan (2014 Period)")


japan.loc[len(japan)-1,"nLx"] = japan.loc[len(japan)-1,"lx"]/japan.loc[len(japan)-1,'nmx'] #fill in lx for open ended cohort

japan['Tx'] = japan.loc[::-1, 'nLx'].cumsum()[::-1] # perform a reverse cumulative sum
japan["ex"] = japan["Tx"] / japan["lx"] # calculate life expectancy at each age group

japan.plot(x="Age", y="ex")
plt.xlabel("Age")
plt.ylabel("Life Expectancy")
plt.title("Life Expectancy for Japan (2014 Period, Adjusted for Open-Ended Cohort)")



