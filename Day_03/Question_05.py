# From the dictionary in Q1, return one list with all scores:
# [85, 90, 88, 78, 81, 79]


students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 81, 79],
}
def average_scores(students):
    l = []
    for scores in students:
        l.extend(students[scores])
    print(l)

average_scores(students)



