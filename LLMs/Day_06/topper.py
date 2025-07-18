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
        student_names = []

        topper_name = '' 
        topper_total = 0
        for line in lines[1:]:  # Skip header
            total_students += 1
            parts = line.strip().split(',')  # e.g. ['IC', '90', '85']
            name = parts[0]


            student_names.append(name)
            total_students += 1
            if parts[1] > parts[2]:
                compare = name
            else:
                compare = name

          

        return jsonify({
            "Topper": compare
        })

    except FileNotFoundError:
        return "marks.csv not found", 404
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
