# Given a dictionary of students and marks:
# students = {
#     "Alice": [85, 90, 88],
#     "Bob": [78, 81, 79],
# }
# Write a function average_scores(d) that returns:{"Alice": 87.67, "Bob": 79.33}
import statistics


students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 81, 79],
}
def average_scores(students):
    avg_dict={}
    for name, marks in students.items():
        average = round(statistics.mean(marks), 2)
        avg_dict[name] = average
    print(avg_dict)
    

average_scores(students)