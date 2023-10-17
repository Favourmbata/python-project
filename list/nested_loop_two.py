
# Basically I need to write a code that prompts for two numbers (Limit and Copies) and then writes all the numbers from 1 (startvalue) up to and including Limit, Copies number of times and I also need to use nested loops.
#
# Then I have to write a function that that prints out a row of numbers separated by tabs, from (startvalue) to and including limit.

limit = int(input("enter your limit "))
copies = int(input("enter your copy:"))
start_value = 1
end_value = 0
results = []
for copy in range(copies):
    while end_value < limit:
        end_value += 1
        results.append(end_value)
    print(results)

