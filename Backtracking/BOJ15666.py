# N과 M (12)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

arr = [0]


def func(cnt):
    if cnt == M:
        for i in range(1, M + 1):
            print(arr[i], end=' ')
        print()
        return

    temp = 0
    for i in range(N):
        if arr[cnt] <= numList[i] and temp != numList[i]:
            temp = numList[i]
            arr.append(numList[i])
            func(cnt + 1)
            arr.pop()


func(0)
