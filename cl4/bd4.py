def calculate_grades(data):
    # Initialize a dictionary to store total scores and count of scores
    scores = {}

    # Process each name and score pair in the data
    for line in data:
        name, score = line.split(',')
        score = int(score)
        
        if name not in scores:
            scores[name] = {'total': 0, 'count': 0}
        
        scores[name]['total'] += score
        scores[name]['count'] += 1

    # Calculate the average score and determine the grade
    results = {}
    for name, info in scores.items():
        average_score = info['total'] / info['count']
        
        if average_score >= 90:
            grade = 'A'
        elif average_score >= 80:
            grade = 'B'
        elif average_score >= 70:
            grade = 'C'
        elif average_score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        results[name] = (average_score, grade)

    return results

# Example usage:
data = [
    "Alice,85",
    "Bob,90",
    "Alice,95",
    "Charlie,70",
    "Bob,85",
    "Charlie,60"
]

grades = calculate_grades(data)
for name, (avg, grade) in grades.items():
    print(f"{name}: Average Score = {avg}, Grade = {grade}")
