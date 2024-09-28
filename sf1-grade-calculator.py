labs = int(input("Enter the number of labs completed: "))
if labs < 0:
    print("ERROR: Number of labs cannot be negative")
else:
    quizzes = int(input("Enter the number of quizzes completed: "))
if quizzes < 0:
    print("ERROR: Number of quizzes cannot be negative")
else:
    assg_1 = float(input("Enter grade for Assignment 1: "))
if assg_1 < 0 or assg_1 > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    assg_2 = float(input("Enter grade for Assignment 2: "))
if assg_2 < 0 or assg_2 > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    assg_3 = float(input("Enter grade for Assignment 3: "))
if assg_3 < 0 or assg_3 > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    assg_4 = float(input("Enter grade for Assignment 4: "))
if assg_4 < 0 or assg_4 > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    midterm_1 = float(input("Enter grade for Midterm 1: "))
if midterm_1 < 0 or midterm_1 > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    midterm_2 = float(input("Enter grade for Midterm 2: "))
if midterm_2 < 0 or midterm_2 > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    final = float(input("Enter grade for Final Exam: "))
if final < 0 or final > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    prep = float(input("Enter grade for Midterms and Final Preparation: "))
if prep < 0 or prep > 100:
    print("ERROR: Grade must be between 0 and 100")
else:
    if labs >= 6:
        labs = 20
    else:
        labs = labs * 20/6
    if quizzes >= 6:
        quizzes = 15
    else: 
        quizzes = quizzes * 15/6
    final = final * 0.18
    prep = prep * 0.06
    assg_t = (assg_1 + assg_2 + assg_3 + assg_4) / 4 * 0.16
    midterm_t = (midterm_1 + midterm_2) / 2 * 0.25

grade = labs + quizzes + assg_t + midterm_t + final + prep
print(f'Your grade is: {round(grade, 2)}')
