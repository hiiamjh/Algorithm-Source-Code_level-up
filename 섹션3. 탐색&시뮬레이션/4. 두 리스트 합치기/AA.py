#import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

#1) 두 리스트를 합쳐서 다시 sorting하는 경우의 O(n): 8log8
answer = sorted(l1+l2)
for i in answer:
    print(i, end=' ')

#2) 이미 오름차순으로 정렬된 두 리스트를 다시 오름차순으로 정렬 시 O(n): 8
'''
p1 = p2 = 0 #포인터 변수
answer = []

while p1 < n and p2 < m: #두 리스트 중 하나를 모두 처리하면 종료
    if a[p1]<=b[p2]:
        answer.append(a[p1])
        p1 += 1
    else:
        answer.append(b[p2])
        p2 += 1
        
if p1 < n:
    answer = answer + a[p1:]
if p2 < m:
    ansewer = answer + b[p2:]

for x in answer:
    print(x, end=' ')
'''