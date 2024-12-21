def calculate_average_marks(students):
    averages = {name: round(sum(marks) / len(marks), 2) for name, marks in students.items()}
    top_performer = max(averages, key=averages.get)
    return averages, top_performer
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
average_marks, top_performer = calculate_average_marks(students)
print(f"Average Marks: {average_marks}")
print(f"Top Performer: \"{top_performer}\"")
