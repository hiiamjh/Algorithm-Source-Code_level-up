#import sys
#sys.stdin=open("input.txt", "r")

answer = []
n = int(input())
temp = list(map(int, input().split()))
answer += temp
m = int(input())
temp = list(map(int, input().split()))
answer += temp
answer.sort()
print(answer)
