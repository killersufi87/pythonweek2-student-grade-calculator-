'''
name = input("Enter student name: ")
marks = input("Enter marks (0-100): ")

#print("Student Name:", name)
#print("Marks:", marks)
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")
marks = int(marks)
if marks >= 90:
    grade = "A"
    message = "Excellent work! 🌟"
elif marks >= 80:
    grade = "B"
    message = "Very Good! Keep it up! 👍"
elif marks >= 70:
    grade = "C"
    message = "Good effort! 😊"
elif marks >= 60:
    grade = "D"
    message = "Needs improvement 💪"
else:
    grade = "F"
    message = "Don't give up! Try again 🚀"
print("\nRESULT")
print("Grade:", grade)
print("Message:", message)
'''
def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! 😊"
    elif marks >= 60:
        return "D", "Needs improvement 💪"
    else:
        return "F", "Don't give up! Try again 🚀"

name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

grade, message = calculate_grade(marks)

print(f"\nRESULT FOR {name.upper()}")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")

