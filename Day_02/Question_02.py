'''Write a function assign_grades(scores) that takes a dictionary like:
python
Copy code
{"Alice": 92, "Bob": 78, "Clara": 65}
And returns a dictionary where values are replaced with grades like:
90+ = A
80-89 = B
70-79 = C
60-69 = D
Below 60 = F'''

scores = {
    "Alice": 92, "Bob": 78, "Clara": 65
}

def assign_grades(scores,keys):
    score = scores.get(keys)
    if score is None:
        print("student not found")
        return
    if score >= 90:
        grade = "A"
    elif score >= 80 and score <=89 :
        grade = "B"
    elif score >=70 and score <= 79 :
        grade = "C"
    elif score >=60 and score <= 69:
        grade = "D"
    else:
        grade = "F"
    new_dict= {}
    new_dict[keys] = grade
    print(new_dict)
for student in scores:
    assign_grades(scores,student)

