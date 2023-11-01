import pandas as pd

t=pd.read_csv("./dataset/Test.csv")

print(t)
t.dropna(inplace=True)
t.drop_duplicates(inplace=True)

t=t[['ID','Ever_Married','Spending_Score','Family_Size']]
print(t)



