# sum = 0
# count = 0
# while True:
#    number =float( input("Enter the number"))
#    sum += number
#    count += 1
#    choice = input("add  another number?(y/n):")
#    if choice.casefold() == 'n':
#        break
#
# sum / number
# print()

student_heights = input("Input a list of students height:").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print("The number of student is ", student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print("Total height is ",total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print("Number of student is ",number_of_students)

average_height = round(total_height / number_of_students)
print("Average height is ",average_height)
