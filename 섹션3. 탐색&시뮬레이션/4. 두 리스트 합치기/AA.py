#import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

answer = sorted(l1+l2)

for i in answer:
    print(i, end=' ')
