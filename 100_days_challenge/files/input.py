try:

    age = int(input("enter ya age: "))
    result = 10 / age
    print(result)
except (ZeroDivisionError,ValueError):
    print("ur age cannot be literal")
finally:
    print("finally block runs either there is exception")





# def age_check(age):
#     if age <= 0:
#         raise ValueError("age cannot be less than or equal to zero")
#     else:
#         return f'you are {age} years old'
#
#
# print(age_check(-3))
