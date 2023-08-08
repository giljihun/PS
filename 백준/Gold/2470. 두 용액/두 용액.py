def find_neuter(arr):
    n = len(arr)
    start, end = 0, n - 1
    min_sum = float('inf') # 가장 작은 합을 저장할 변수 초기화
    answer = None # 가장 작은 합을 가진 두 용액의 번호를 저장할 변수 초기화

    while start < end:
        current_sum = arr[start] + arr[end]
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            answer = (arr[start], arr[end])
        if current_sum < 0:
            start += 1
        else:
            end -= 1

    print(answer[0], answer[1])

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
find_neuter(arr)
