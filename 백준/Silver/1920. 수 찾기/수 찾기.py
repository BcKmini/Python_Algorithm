import sys

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(binary_search(A, target))