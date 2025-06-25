students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 81, 79],
}
def highest_scores(students):
    highest = {}
    for name, scores in students.items():
        highest[name] = max(scores)
    print("'name':{name}, 'highest score':{score}" .format(name=name, highest=highest))

highest_scores(students)