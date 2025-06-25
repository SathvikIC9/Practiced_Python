students = {
    "Alice": {"math": 90, "science": 85},
    "Bob": {"math": 78, "science": 82},
}
def calculate_average(students):
    totals = {"math": 0, "science": 0}
    count = 0

    for student, subjects in students.items():
        totals["math"] += subjects["math"]
        totals["science"] += subjects["science"]
        count += 1

    averages = {
        "math": totals["math"] / count,
        "science": totals["science"] / count
    }

    return averages

print(calculate_average(students))