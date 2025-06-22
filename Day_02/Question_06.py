students = {
    "John": {"math": 90, "science": 85},
    "Alice": {"math": 78, "science": 92}
}

def get_score(name, subject):
    if name in students and subject in students[name]:
        print(students[name][subject])
    else:
        print("Not found")
get_score(name="John", subject="math")