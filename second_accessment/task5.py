first_name = input("enter first name: ")
last_name = input("Enter last name: ")
surname = first_name + last_name
print(surname[::-1])

first_name, last_name = input("Enter your first name and last name: ").split(" ", 2)

first_name = first_name[::-1]
last_name = last_name[::-1]

print(f"{first_name} {last_name}")
