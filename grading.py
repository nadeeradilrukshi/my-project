def calculate_grade(score):
    if not (0 <= score <= 100):
        return "Invalid score"
    elif 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

# Example scores (adjusted to be in the range [0, 100])
scores = [85, 92, 78, 60, 45, 35, 105, -5]

# Calculate and print grades
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score}, Grade: {grade}")
