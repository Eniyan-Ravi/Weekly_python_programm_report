#student mark analysis using numpy
import numpy as np

marks = np.array([78, 85, 92, 67, 88, 95, 73, 81, 90, 76])

print("Student Marks")
print(marks)

print("\nShape:", marks.shape)
print("Size:", marks.size)
print("Data Type:", marks.dtype)

print("\nHighest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))

print("\nStudents scoring above 80:")
print(marks[marks > 80])

print("\nAdding Grace Marks (+5):")
print(marks + 5)

print("\nPercentage (Out of 100):")
print(marks / 100)

print("\nSorted Marks:")
print(np.sort(marks))