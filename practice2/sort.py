l1 = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
print("Original list", l1)

for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]
print(l1)
l = len(l1)
if l % 2 == 0:
    m1 = l1[l // 2]
    m2 = l1[l // 2]
    mid = (m1 + m2) / 2
    print(mid)
else:
    mid = l1[l // 2]
# print(mid)
# total = 0
# for a in l1:
#     total += a
#     mean = total / l
# print(mean)
