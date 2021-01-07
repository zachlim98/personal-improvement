import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 


pop = 7.594 #in billions
growth_rate = 1.0124
yearlist = []
poplist = []

for i,d in enumerate(np.arange(2021,2051)):
    year = d
    pop = pop * growth_rate**(i+1)
    yearlist.append(year)
    poplist.append(pop)

pop_growth = pd.DataFrame(
    {
        "Year" : yearlist,
        "Population" : poplist
    }
)

plt.plot(pop_growth.Year, pop_growth.Population)
plt.xlabel("Year")
plt.ylabel("Population Size")
plt.title("World Population Projected Growth")


constant = np.log(2) # we use 2 since the new population size will be 2 times the old population size

R = 0.0124

doubletime = constant/R
print("get_ipython().run_line_magic(".2f", " years\" % (doubletime))")


japanew = pd.read_csv(R"./Resources/japanew.csv") #import sample dataset
japanew["Japan_MX"] = japanew.iloc[:,1]/japanew.iloc[:,2] #create Japan death rate
japanew["EngW_MX"] = japanew.iloc[:,3]/japanew.iloc[:,4] #create England Wales death rate

#create log death rate
japanew["Japan_Lg_MX"] = np.log(japanew["Japan_MX"])
japanew["EngW_Lg_MX"] = np.log(japanew["EngW_MX"])

#age structure
japanew["Japan_AgeStr"] = japanew.iloc[:,2]/japanew.iloc[:,2].sum() 
japanew["EngW_AgeStr"] = japanew.iloc[:,4]/japanew.iloc[:,4].sum() 
japanew["MeanAgeStr"] = (japanew["Japan_AgeStr"]+japanew["EngW_AgeStr"])/2

#calculate standardized death rate
japanew["Japan_Std_DR"] = japanew["MeanAgeStr"]*japanew["Japan_MX"]
japanew["EngW_Std_DR"] = japanew["MeanAgeStr"]*japanew["EngW_MX"]

jap_std_DR = japanew["Japan_Std_DR"].sum()
ew_std_DR = japanew["EngW_Std_DR"].sum()

print("Japan Standardized Death Rate: get_ipython().run_line_magic(".5f"", " %jap_std_DR)")
print("England/Wales Standardized Death Rate: get_ipython().run_line_magic(".5f"", " %ew_std_DR)")


ax = plt.gca()

japanew.plot(kind="line",x="age",y="Japan_MX",label="Japan", ax=ax)
japanew.plot(kind="line",x="age",y="EngW_MX",label="England/Wales", ax=ax)
plt.title("Age Specific Death Rates")
plt.ylabel("Death Rates")
plt.xlabel("Age")


jap_std_DR = ((japanew.iloc[:,1]/japanew.iloc[:,2])*((japanew.iloc[:,2]/japanew.iloc[:,2].sum()+japanew.iloc[:,4]/japanew.iloc[:,4].sum())/2)).sum()
ew_std_DR = ((japanew.iloc[:,3]/japanew.iloc[:,4])*((japanew.iloc[:,4]/japanew.iloc[:,4].sum()+japanew.iloc[:,2]/japanew.iloc[:,2].sum())/2)).sum()

print("Japan Standardized Death Rate: get_ipython().run_line_magic(".5f"", " %jap_std_DR)")
print("England/Wales Standardized Death Rate: get_ipython().run_line_magic(".5f"", " %ew_std_DR)")



