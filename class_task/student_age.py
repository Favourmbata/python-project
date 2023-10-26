students = {"Dike": 33, "Ope": 25, "Melody": 20, "Precious": 27}


def student_age_name():
    name = input("Enter your name: ").lower()
    for student in students.keys():
        if student == name:
            return f"Hi,{name}your age is {students.get(student)}"
        else:
            while name not in students.keys():
                age = (input("Name not found,enter your age: "))
                students.update({name: age})
                return f"hi,{name} your age is {students.get(name)}"


# print(student_age_name())
if __name__ == '__main__':
    student_age_name()
print(students)

#
#
# if __name__ == '__main__':
#     student_age_name
#

#
# student_age = {"Dike": 33, "Ope": 25, "Melody": 20, "Precious": 27}
# keys = {"precious": 27}
# name = input("Enter your name: ")
# for name in student_age:
#     if name == student_age:
#         print(keys)
#
# student_age = {k: student_age[k] for k in student_age.keys()}
# print(student_age)
