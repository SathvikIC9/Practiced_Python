students = {

    "Alice": {"math": 90, "science": 85},
    "Bob": {"math": 78, "science": 82},
}
def normalize(students):
    for name in students:
        students[name] = [round(score * 100 / 120, 2) for score in students[name]]
    return students
print(normalize(students))  # Output: {'Alice': [75.0, 70