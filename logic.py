# modified logic from lab 2
import csv
import os.path


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


def survey(name, scorlist):
    liste = []
    stats = check_stats(scorlist)
    average = float(f'{stats[0]:.2f}')
    # top = stats[1]
    # grade = check_grade(average, top)

    liste.append(name)
    liste += scorlist
    while len(liste) < 5:
        liste.append(0)
    liste.append(average)
    # liste.append(grade)

    if not os.path.isfile('output.csv'):
        with open('output.csv', 'w', newline='') as csvfile:
            csv.writer(csvfile).writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Average'])
        csvfile.close()
    if os.path.isfile('output.csv'):
        with open('output.csv', 'a', newline='') as csvfile:
            csv.writer(csvfile).writerow(liste)
