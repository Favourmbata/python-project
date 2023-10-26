# def your_salary():
teacher_name = input("Enter teachers name:")
number_of_period_taught = int(input("Enter period taught: "))
rate_per_period = int(input("Enter rate: "))
monthly_gross_salary = number_of_period_taught * rate_per_period
currently_monthly_rate = 20
overtime = 25
if number_of_period_taught > 100:
    print(overtime * number_of_period_taught + overtime)
else:
    print(number_of_period_taught * rate_per_period)

print(overtime)

print("Teacher:", teacher_name)
print("periods taught is :", number_of_period_taught)
print("Gross salary is:", monthly_gross_salary)

# if __name__ == '__main__':

# your_salary()
