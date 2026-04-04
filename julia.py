#step1:import required libraries
import pandas as pn
#step2:load the dataset
data=pn.read_csv("salary_dataset.csv")
#step3:exprole the dataset (understandiing the data before training)
rows = data.head()
print(rows)
nbr=data.shape
print(nbr)
#displaying column names
cols=data.columns
print(cols)
#detailed info
details=data.info()
print(details)
#statistical summary in data
statistics =data.describe()
print (statistics)
#step4:data cleaning
#dispaly missing values
missing_values=data.isnull().sum()
print (missing_values)
#filling the missing values
data["Salary"].fillna(data["Salary"].mean(), inplace=True)
#delete missing values in datasets
data.drop_duplicates(inplace=True)

# displaying cleaned
cleaned = data.tail()
print(cleaned)
  #displaying cleaned
cleaned=data.tail()
print (cleaned)                  

#step5:split data int training and testing sets
#step6:model selection 
#step7:training the model
#step8:model evaluation
#step9:prediction of outcomes
#step10:deployment