# Project 2 Solution: Grade Manager

\`\`\`python
def load_grades(filename):
    grades = {}
    with open(filename, 'r') as f:
        for line in f:
            name, grade = line.strip().split(',')
            grades[name] = int(grade)
    return grades

def calculate_stats(grades):
    if not grades:
        return None
    
    values = list(grades.values())
    return {
        'average': sum(values) / len(values),
        'max': max(values),
        'min': min(values),
        'count': len(values)
    }

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def grade_distribution(grades):
    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades.values():
        letter = get_letter_grade(grade)
        dist[letter] += 1
    return dist

# Main
grades = load_grades("grades.txt")
stats = calculate_stats(grades)
dist = grade_distribution(grades)

print(f"Average: {stats['average']:.2f}")
print(f"Distribution: {dist}")
\`\`\`

---
