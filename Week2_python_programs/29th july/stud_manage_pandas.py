#student management system using pandas
import pandas as pd

students = {
    "ID": [101,102,103,104,105],
    "Name": ["eniyan","bob","ravi","David","tunya"],
    "Age": [21,22,20,23,22],
    "Marks": [85,90,78,95,88]
}

df = pd.DataFrame(students)

print("Student Details")
print(df)

print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nFirst 3 Students")
print(df.head(3))

print("\nStudents Scoring Above 85")
print(df[df["Marks"] > 85])

print("\nHighest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Marks:", df["Marks"].mean())