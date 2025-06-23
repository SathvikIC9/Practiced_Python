# Return the student with the highest total score (name only).
import statistics


students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 81, 79],
}
avg_dict={}
def average_scores(students):
    for name, marks in students.items():
        average = round(statistics.mean(marks), 2)
        avg_dict[name] = average
    print(avg_dict)
    for name, average in avg_dict.items():
        if average >= 80 :
            print(f"{name} has passed the course")
        else:
            print(f"{name} has failed the course")

def max_marks(avg_dict):
    print(max(avg_dict , key=avg_dict.get))
    

average_scores(students)
max_marks(avg_dict)