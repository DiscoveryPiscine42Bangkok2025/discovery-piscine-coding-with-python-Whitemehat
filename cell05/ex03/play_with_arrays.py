num = [2, 8, 9, 48, 8, 22, -12 ,2]
n_num = []
u_num = []
count = 0
for i in range(len(num)):
    if num[i] + 2 > 5:
        n_num.append(num[i] + 2)

for j in range(len(n_num)):
    found = 0
    for k in range(count):
        if n_num[j] == u_num[k]:
            found = 1
            break
    if not found:
        u_num.append(n_num[j])
        count += 1

print(u_num)