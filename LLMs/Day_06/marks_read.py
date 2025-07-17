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

        for line in lines[1:]:  # Skip header
            total_students += 1
            parts = line.strip().split(',')  # e.g. ['IC', '90', '85']

            for i, subject in enumerate(subjects):
                subject_totals[subject] += int(parts[i+1])  # i+1 skips the name

        # Now calculate averages
        subject_averages = {
            subject: subject_totals[subject] // total_students
            for subject in subjects
        }

        return jsonify({
            "total_students": total_students,
            "subject_averages": subject_averages
        })

    except FileNotFoundError:
        return "marks.csv not found", 404
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
