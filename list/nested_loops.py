# I have to make two class lists, one with Maths students and the other with Computer Science students.
#



mathStudents = ['Audrey', 'Ben', 'Julia', 'Paul', 'Gerry', 'Sue', 'Helena', 'Harry', 'Marco', 'Rachel', 'Tina', 'Mark',
                'Jackson']

csStudents = ['William', 'Ariel', 'Melissa', 'Sue', 'Ben', 'Audrey', 'Susan', 'Mark', 'Hemi', 'Brendan', 'Paul',
              'Barry', 'Julia']
common_class = []
for students in mathStudents:
    for students in csStudents:
        if csStudents == mathStudents:
            common_class.append(mathStudents)
    print(common_class)

#  I need to use these lists in nested loops to find out which students are enrolled in both classes and count the total number of students.
#
# My output should look like the following:
#
#
# Student: Audrey is enrolled in both classes
# Student: Ben is enrolled in both classes
# Student: Julia is enrolled in both classes
# Student: Paul is enrolled in both classes
# Student: Sue is enrolled in both classes
# Student: Mark is enrolled in both classes
#
# 6  students are enrolled in Computer Science and Maths
