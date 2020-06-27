# pandas is a library written for the Python for data manipulation and analysis
import pandas as pd
adm=pd.read_csv('Admission_Predict.csv')
adm.head()
print(adm)

# loc
print(adm.loc[3, 'GRE Score'])

# iloc
print(adm.iloc[3, 1])
print(adm.iloc[0:3, 0:3])

# find the unique values in GRE score
GRE = adm['GRE Score'].unique()
print(GRE)
print(len(GRE))

# find GRE value >= 337
print(adm['GRE Score'] >= 337)
adm1 = adm[adm['GRE Score'] >= 337]
print(adm1)