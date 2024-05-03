# modified logic from lab 2
import csv
import os.path

'''
Finds average letter-grade based on average scores and top score 
:score: Average score
:top: The Highest Score
:return: returns the letter grade based on calculations
'''


def check_grade(score, top):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


'''
Finds average of student scores and highest score
:scores: the list of scores taken from survey()
:return: The average of the scores as well as top score
'''


def check_stats(scores):
    av = 0
    top = 0
    for i in scores:
        av += float(i)
        if float(i) >= float(top):
            top = i
    return (av / len(scores)), top


'''
Takes data from gui file and uses it to get average of scores
:name: name of the student entered by user in gui
:scorlist: list of scores entered by user in gui
This function has no return but writes /appends student score data to 'output.csv'
'''


def survey(name, scorlist):
    liste = []
    stats = check_stats(scorlist)
    average = float(f'{stats[0]:.2f}')
    top = stats[1]
    grade = check_grade(average, top)

    # Liste = [Name] + [Scores] + [Average]
    liste.append(name)
    liste += scorlist
    while len(liste) < 5:
        liste.append(0)
    liste.append(average)
    liste.append(grade)

    # Write scores data to 'output.csv'
    if not os.path.isfile('output.csv'):
        with open('output.csv', 'w', newline='') as csvfile:
            csv.writer(csvfile).writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Average'])
        csvfile.close()
    if os.path.isfile('output.csv'):
        with open('output.csv', 'a', newline='') as csvfile:
            csv.writer(csvfile).writerow(liste)
