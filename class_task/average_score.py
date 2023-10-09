# def average_score(scores):
#     total = 0
#     score = float(input("Enter scores"))
#     for number in score:
#         total += score
#         average = total / len(average)
#         # return average
#     print("The average is ", average)


def average_score(scores):
    return sum(scores) / len(scores)


exam_score = []
for i in range(10):
    score = int(input("Enter your score:"))
    exam_score .append(score)
print(average_score(exam_score))

# def me(name: str,number:int,age: int)-> str:
#     x = 2+ 3
#     me("yoy",2000,21)
#     me(name="yoy",number= 2323,age= 21)
#
#     name = "joe"
#     if name :
#          x = 2 + 3