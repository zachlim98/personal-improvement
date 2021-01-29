import pandas as pd
import numpy as np 

brazil = pd.read_csv(R"./Resources/brazil.csv").replace(to_replace=0.00,value=np.nan).dropna() #import data file and get rid of non-reproductive ages
brazil["daughter_ASFR"] = brazil["Age-specific fertility rate"]*(100/(105+100)) #convert to daughter-specific ASFR by multiply by sex ratio at birth 

GRR = brazil["daughter_ASFR"].sum()*5/1000 #multiply by 5 since 5 ages per bracket, and per thousand
print("Gross Reproduction Rate is: {:.2f}".format(GRR))


brazil["Lx"] = brazil["Lx"].astype('str').str.replace(' ','').astype('int')
brazil["daughter_ASFR_mort"] = brazil["daughter_ASFR"] * (brazil["Lx"]/500000)

NRR = brazil["daughter_ASFR_mort"].sum()*5/1000 #multiply by 5 since 5 ages per bracket, and per thousand
print("Net Reproduction Rate is: {:.2f}".format(NRR))


brazil["Tot_birth"] = brazil["daughter_ASFR_mort"] * (brazil["age"]+2.5)
MAC = sum(brazil["Tot_birth"])/sum(brazil["daughter_ASFR_mort"])
r = np.log(NRR)/MAC
print("The intrinsic rate of natural increase is {:.4f}".format(r))
