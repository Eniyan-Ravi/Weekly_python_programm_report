

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i+1}")

    name = input("Enter Name: ")
    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    total = math + science + english
    average = total / 3

    # Grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    # Result
    if math < 35 or science < 35 or english < 35:
        result = "Fail"
    else:
        result = "Pass"

    students.append([name, math, science, english, total, average, grade, result])

while True:
    print("\n1. Student Information")
    print("2. Overall Information")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        search = input("Enter student name: ")

        found = False
        for student in students:
            if student[0].lower() == search.lower():
                print("")
                print("Name:", student[0])
                print("Total:", student[4])
                print("Average:", round(student[5], 2))
                print("Grade:", student[6])
                print("Result:", student[7])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 2:
        # Top Scorer
        top = students[0]
        for student in students:
            if student[4] > top[4]:
                top = student

        # Class Average
        sum_avg = 0
        for student in students:
            sum_avg += student[5]
        class_avg = sum_avg / len(students)

        # Passes and Fails
        passes = 0
        fails = 0
        for student in students:
            if student[7] == "Pass":
                passes += 1
            else:
                fails += 1

        highest = students[0][1]
        lowest = students[0][1]

        for student in students:
            for mark in student[1:4]:
                if mark > highest:
                    highest = mark
                if mark < lowest:
                    lowest = mark
        print("")
        print("Top Scorer:", top[0], "-", top[4])
        print("Class Average:",class_avg, 2)
        print("Number of Passes:",passes)
        print("Number of Fails:",fails)
        print("Highest Subject Mark:",highest)
        print("Lowest Subject Mark :",lowest)

    elif choice == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")