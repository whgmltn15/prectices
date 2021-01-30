grade_list = {'A+' : 4.5, 'A0' : 4.2 , 'A-': 4.0,
              'B+' : 3.5, 'B0' : 3.2 , 'B-': 3.0,
              'C+' : 2.5, 'C0' : 2.2 , 'C-': 2.0,
              'D+' : 1.5, 'D0' : 1.2 , 'D-': 1.0,
              "F": 0.5}

grades = ["DS7651 A0", "CA0055 D+", "AI5543 C0",
         "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-",
          "AI5543 D+", "DS7651 A+", "OS1808 B-"]

newGrades = []
def GradeA():
    for i in range(len(grades)):
        subject = grades[i].split(' ')[0]
        grade = grades[i].split(' ')[1]

        check = True
        for j in range(len(newGrades)):
            newSubject = newGrades[j].split(' ')[0]
            newGrade = newGrades[j].split(' ')[1]

            if subject == newSubject:
                check = False
                if grade_list[newGrade] < grade_list[grade]:
                    newGrades[j] = newSubject + " " + grade
        if check:
            newGrades.append(subject + " " + grade)

def newGradesB():
    for i in range(len(newGrades)):
        for j in range(len(newGrades)-1):
            currentGrade = newGrades[i].split(' ')[1]
            afterGrade = newGrades[j].split(' ')[1]

            if grade_list[currentGrade] > grade_list[afterGrade]:
                newGrades[i], newGrades[j] = newGrades[j], newGrades[i]
