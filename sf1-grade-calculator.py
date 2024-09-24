labs = int(input("Enter the number of labs completed: "))
quizzes = int(input("Enter the number of quizzes completed: "))

if labs >= 6:
    labs = 20
else:
    labs = labs * 20/6

if quizzes >= 6:
    quizzes = 15
else:
    quizzes = quizzes * 15/6

assg_1 = float(input("Enter grade for Assignment 1: "))
assg_2 = float(input("Enter grade for Assignment 2: "))
assg_3 = float(input("Enter grade for Assignment 3: "))
assg_4 = float(input("Enter grade for Assignment 4: "))
assg_t = (assg_1 + assg_2 + assg_3 + assg_4) / 4 * 0.16

midterm_1 = float(input("Enter grade for Midterm 1: "))
midterm_2 = float(input("Enter grade for Midterm 2: "))
midterm_t = (midterm_1 + midterm_2) / 2 * 0.25

final = float(input("Enter grade for Final Exam: "))
final = final * 0.18

prep = float(input("Enter grade for Midterms and Final Preparation: "))
prep = prep * 0.06

grade = labs + quizzes + assg_t + midterm_t + final + prep
print(f'Your grade is: {round(grade)}')


# ask Qs: labs and quizzes (100 or 0), labs and quizzes 6 or more, 5 or more
# grade total: integer?
