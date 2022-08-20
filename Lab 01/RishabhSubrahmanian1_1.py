'''
Write a program to prompt for a score between 0 and 100. If the score is out of range,
print an error message, else use the grading system below.
score >= 90 = A
score >= 80 = B
score >= 70 = C
score >= 60 = D
score < 60 = F
Your program should use a function to determine the letter grade and a loop to allow the
user to enter a new score until they decide to stop the program.
Please note:
• Numeric input should be treated as a float.
• Strip your string input and make sure you are accounting for upper and lower case
input
'''

def grade_output(grade):
    if grade < 0 or grade > 100:
        print('Invalid score')
    elif grade >= 90:
        print('Grade = A')
    elif grade >= 80:
        print('Grade = B')
    elif grade >= 70:
        print('Grade = C')
    elif grade >= 60:
        print('Grade = D')
    else:
        print('Grade = F')

while True:
    score = float(input('Enter a score: '))
    grade_output(score)
    yes_no = str(input('Continue (y/n): '))
    while yes_no != 'y' and yes_no != 'n':
        yes_no = str(input('Enter \'y\' or \'n\': '))

    if yes_no == 'n':
        print('End of program')
        break
