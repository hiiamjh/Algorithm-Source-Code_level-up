#import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
max_val = n
n_list = []

for i in range(n):
    n_list.append(list(map(int, input().split())))

temp = 0
for i in range(len(n_list)):
    temp += n_list[i][i]
    if sum(n_list[i]) > max_val:
        max_val = sum(n_list[i])
    if i == len(n_list)-1:
        if temp > max_val:
            max_val = temp

n_list_t = [list(x) for x in zip(*n_list)]

temp = 0
for i in range(len(n_list_t)):
    temp += n_list_t[i][i]
    if sum(n_list_t[i]) > max_val:
        max_val = sum(n_list_t[i])
    if i == len(n_list_t)-1:
        if temp > max_val:
            max_val = temp

print(max_val)
