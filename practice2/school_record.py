Average_score = 0
Total_score = 0
score = 0
while score <= 20:
    score = int(input("Enter  student average score "))
    if score >= 0 or score <= 100:
        break
    Average_score = Total_score / 20
    Total_score += score
print("********************************************")
print("ASO ROCK SECONDARY SCHOOL,ABUJA NIGERIA")
print("Class:sss 3")
print("Number of Student in class:")
print("Total score is:", Total_score)
print("Average score is:", Average_score)
print("************************************************")
