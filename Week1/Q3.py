class Grades:
    def printGrade(score):
        if score >= 90.0 and score <= 100.0:
            print("Grade A")
        elif score >= 80.0 and score < 90.0:
            print("Grade B")
        elif score >=70.0 and score < 80.0:
            print("Grade C")
        elif score >= 60.0 and score < 70.0:
            print("Grade D")
        elif score >=0 and score < 60.0:
            print("Grade F")
if __name__ == "__main__":
    grade = float(input())
    Grades.printGrade(grade)