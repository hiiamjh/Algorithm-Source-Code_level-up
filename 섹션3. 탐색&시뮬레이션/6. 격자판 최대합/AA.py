#import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
max_val = n #격자판 원소=자연수
n_list = []

#)행과 열을 따로 탐색
for i in range(n):
    n_list.append(list(map(int, input().split())))
'''
n_list = [list(map(int, input().split())) for _ in range(n)]
for x in n_list:
    print(x) #행별 출력
'''

temp = 0
for i in range(len(n_list)):
    temp += n_list[i][i]
    if sum(n_list[i]) > max_val: #행의 최댓값
        max_val = sum(n_list[i])
    if i == len(n_list)-1:
        if temp > max_val: #왼쪽 대각선의 합
            max_val = temp

n_list_t = [list(x) for x in zip(*n_list)] #전치

temp = 0
for i in range(len(n_list_t)):
    temp += n_list_t[i][i]
    if sum(n_list_t[i]) > max_val: #열의 최댓값
        max_val = sum(n_list_t[i])
    if i == len(n_list_t)-1:
        if temp > max_val: #오른쪽 대각선의 합
            max_val = temp

print(max_val)

#)행과 열을 한번에 탐색
'''
largest = -2147000000 #정수의 최솟값
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += n_list[i][j] #행의 최댓값
        sum2 += n_list[j][i] #열의 최댓값
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i] #왼쪽 대각선의 최댓값
    sum2 ++ a[i][n-i-1] #오른쪽 대각선의 최댓값
if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
print(largest)
'''
