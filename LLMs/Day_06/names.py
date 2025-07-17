from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/summarycsv')
def summary():
    try:
        with open('marks.csv', 'r') as file:
            lines = file.readlines()

        # First line is the header
        header = lines[0].strip().split(',')  # ['Name', 'Maths', 'Science']
        subjects = header[1:]  # ['Maths', 'Science']

        total_students = 0
        subject_totals = {subject: 0 for subject in subjects}
        student_names = []

        for line in lines[1:]:  # Skip header
            parts = line.strip().split(',')  # e.g. ['IC', '90', '85']
            name = parts[0]


            student_names.append(name)
            total_students += 1
        

            # for i, subject in enumerate(subjects):
            #     subject_totals[subject] += (parts[i])  # i+1 skips the name

        # Now calculate averages
        # subject_averages = {
        #     subject: subject_totals[subject] // total_students
        #     for subject in subjects
        # }

        return jsonify({
            "total_students": total_students,
            "names": student_names
        })

    except FileNotFoundError:
        return "marks.csv not found", 404
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
