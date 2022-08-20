'''
The list below contains the scores of different students.

items = ['James:45.5', 'Jill:70', 'John:90']

Each element in the list is a combination of a student name and their corresponding score
(the score comes after the : character). Translate the list to a dictionary where the
student’s name is stored as a key and the score is stored as the corresponding value. Once
done, compute and display the total and average score of all the students. The output of
your program should be identical to the sample output below.
Please note:
• Numeric output must be displayed to 2 decimal places.
• You should generate the dictionary through code, not hard coding its keys or
values.
• Write a program that would still work if the list had more elements added to it
(make your code flexible).
'''


items = ['James:45.5', 'Jill:70', 'John:90', ]
_dict = {}
for i in items:
    j = i.split(':')
    _dict[j[0]] = float(j[1])

total = sum(_dict.values())

print(f'Student scores = {_dict}')
print(f'Scores total = {total:.2f}')
print(f'Scores average = {(total / len(_dict)):.2f}')
