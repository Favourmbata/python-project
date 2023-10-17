# my_list = []
# new_list = [[0 for  column in range(3)] for row in range(2)]
#
# for row in range(2):
#     for column in range(3):
#         new_list[row][column] = row * column
#
#         # print(f"[{row}] [{column}] = {row * column }",end= " ")
#     print()
# print(new_list)
#
total = 0
overal = 0
student_ave = 0
total_student = 0
average = [[25, 50, 75],
           [40, 50, 60],
           [75, 65, 80]]
for v in average:
    student_ave = sum(v) / len(v)
    total += sum(v)
    total_student += len(v)
overal = total / total_student
print(student_ave)
print(overal)
