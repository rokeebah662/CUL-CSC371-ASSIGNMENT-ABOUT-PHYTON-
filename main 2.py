
students = [
    ["ST001", "Computer Science", 300, 85, 78],
    ["ST002", "Cyber Security", 300, 90, 82],
    ["ST003", "Computer Science", 300, 75, 69],
    ["ST004", "Information Technology", 300, 80, 74],
    ["ST005", "Cyber Security", 300, 70, 65],
    ["ST006", "Computer Science", 300, 95, 88],
    ["ST007", "Information Technology", 300, 60, 58],
    ["ST008", "Computer Science", 300, 88, 80],
    ["ST009", "Cyber Security", 300, 78, 72],
    ["ST010", "Information Technology", 300, 92, 85]
]

print("=" * 95)
print("                 STUDENT PERFORMANCE DATASET")
print("=" * 95)

print(f"{'ID':<10} {'DEPARTMENT':<28} {'LEVEL':<8} {'ATTENDANCE':<15} {'EXAM SCORE':<12}")

print("-" * 95)

for student in students:
    print(f"{student[0]:<10} {student[1]:<28} {student[2]:<8} {student[3]:<15} {student[4]:<12}")

print("=" * 95)
print("Total number of students:", len(students))
print("Dataset displayed successfully!")
