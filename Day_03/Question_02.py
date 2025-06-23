# 2. Filter Passed Students
# From the above dict, return a list of names where the average is above 80.
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
    for name, average in avg_dict.items():
        if average >= 80 :
            print(f"{name} has passed the course")
        else:
            print(f"{name} has failed the course")
    

average_scores(students)