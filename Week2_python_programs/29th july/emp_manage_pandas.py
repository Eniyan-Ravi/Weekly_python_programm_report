# employee management system using pandas
import pandas as pd

employee = {
    "Emp_ID":[1,2,3,4,5],
    "Name":["eniyan","tunya","raymond","David","surash"],
    "Department":["IT","HR","IT","Sales","HR"],
    "Salary":[50000,45000,65000,40000,48000]
}

df = pd.DataFrame(employee)

print("Employee Details")
print(df)

print("\nSecond Employee")
print(df.loc[1])

print("\nThird Employee using iloc")
print(df.iloc[2])

df["Bonus"] = df["Salary"] * 0.10

print("\nAfter Adding Bonus")
print(df)

df.loc[0,"Salary"] = 55000

print("\nUpdated Salary")
print(df)

print("\nSorted by Salary")
print(df.sort_values("Salary",ascending=False))

print("\nStatistics")
print(df.describe())