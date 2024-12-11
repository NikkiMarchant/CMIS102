#  Nicole Marchant CMIS 102 6980 Week 5 Assignment
#  calculates students weighted grades.

def student_input(student):
    print(student)
    discussion = eval(input('Please enter discussion grade:'))
    quiz = eval(input('PLease enter quiz grade:'))
    assignment = eval(input('Please enter assignment grade:'))
    return calculation(discussion, quiz, assignment)  # calling calculation


def calculation(discussion_grade, quiz_grade, assignment_grade):
    wt_avg_grade = discussion_grade * 0.15 + quiz_grade * 0.35 + assignment_grade * 0.5
    return wt_avg_grade


def main():
    highest_avg = 0
    top_student = ''
    students = ['Alexi', 'Matteo', 'Nikki', 'Dezy']
    for student in students:
        student_avg = student_input(student)  # calling a function to retrieve student input
        if student_avg > highest_avg:
            highest_avg = student_avg
            top_student = student
    print('The student with the highest average is:', top_student, highest_avg)


if __name__ == '__main__':
    main()
