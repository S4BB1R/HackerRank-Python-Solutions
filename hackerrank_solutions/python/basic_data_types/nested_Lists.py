"""
Problem: Nested List
Difficulty: [Easy]
Category: [Basic Data Types]
URL: [https://www.hackerrank.com/challenges/nested-list/problem]

Description:
[Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.]

"""

def nestedList():
    num_students = int(input())
    students = []
    for i in range(num_students):
        name = input()
        score = float(input())
        students.append([name,score])
    grades = []
    for student in students:
        grades.append(student[1])
    unique_grades=list(set(grades))
    unique_grades.sort()
    second_lowest_grade= unique_grades[1]
    names = []
    for student in students:
        if student[1]==second_lowest_grade:
            names.append(student[0])
    names.sort()
    for name in names:
        print(name)

if __name__ == '__main__':
    nestedList()
