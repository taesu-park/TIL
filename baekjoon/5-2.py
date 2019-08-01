N_list = []
for i in range(9):
    N = int(input())
    N_list.append(N)
# print(max(N_list))
# print(N_list.index(max(N_list))+1)
count = 0
max_num = 0

for j in range(len(N_list)):    
    if max_num < N_list[j]:
        max_num = N_list[j]
        count = j + 1

print(count)
print(max_num)