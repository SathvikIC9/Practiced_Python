# From that list, return a dictionary of score → frequency.
students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 81, 79],
}
def average_scores(students):
    s = []
    for scores in students.values():
        s.extend(scores)
    return s

# average_scores(students)
def frequency_scores(students):
    s =average_scores(students)
    freq = {}
    for score in s:
        if score in freq:
            freq[score] += 1
        else:
            freq[score] = 1
    print(freq)         


frequency_scores(students)



