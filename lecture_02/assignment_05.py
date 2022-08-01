correct_answers = int(input("The number of correct answers: "))
questions = int(input("The total number of questions: "))
grade = correct_answers / questions * 100
if grade >= 90:
    print("A")
elif 90 > grade >= 75:
    print("B")
elif 75 > grade >= 60:
    print("B")
elif 60 > grade >= 45:
    print("C")
elif 45 > grade >= 30:
    print("D")
else:
    print("E")