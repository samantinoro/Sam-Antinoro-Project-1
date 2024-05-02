# modified logic from lab 2

def check_stats(scores):
    av = 0
    top = 0
    for i in scores:
        av += float(i)
        if float(i) >= float(top):
            top = i
    return (av / len(scores)), top


def check_grade(score, top):
    markoff = float(top) - float(score)
    if markoff <= 10:
        grade = 'A'
    elif markoff <= 20:
        grade = 'B'
    elif markoff <= 30:
        grade = 'C'
    elif markoff <= 40:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def scores_get(num_stud):
    scores = input(f'Enter {num_stud} score(s): ')
    scorlist = scores.split()

    for i in scorlist:
        if not i.isdigit():
            scorlist.remove(i)

    while len(scorlist) < num_stud:
        scorlist = scores_get(num_stud)
    for i in range(len(scorlist) - num_stud):
        scorlist.pop()
    return scorlist


def survey(scorlist):
    stats = check_stats(scorlist)
    average = stats[0]
    top = stats[1]

    for i in range(len(scorlist)):
        grade = check_grade(float(scorlist[i]), top)
        print(f'Student {i + 1} score is {scorlist[i]} and grade is {grade}')
    grade = check_grade(average, top)
    print(f'The average score is {average:.2f}, a grade of {grade}')
