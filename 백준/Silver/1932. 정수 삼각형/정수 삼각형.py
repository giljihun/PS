def solution(triangle):
    answer = 0

    # dp 테이블 초기화 & 꼭대기값 삽입
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    # 전체 배열 순회
    for i in range(0, len(triangle) - 1):
        # 각 줄마다 순회(triangle[i] --> 0번 배열, 1번 배열 ...)
        for j in range(len(triangle[i])):
            # i가 0일때를 예로 들어보자,
            # dp[1][0]의 값을 결정해야한다.
            # 그러면 dp[1][0](기존값)과 dp[0][0]에 triangle[1][0](삼각형의 값, 여기선 3)을 더했을 때 값 중 무엇이 큰 지를 보는거다!

            # 왼쪽아래로 뻗은 경우.
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])

            # 오른쪽아래로 뻗은 경우.
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

            # ----> 이런식으로 모든 값을 업데이트!

    # 마지막 배열에 가장 큰 값들이 다 뭉쳐있기 때문에, 그 중 가장 큰 값을 return!
    answer = max(dp[-1])

    print(answer)

n = int(input())
triangle = []

for i in range(0, n):
    a = list(map(int, input().split()))
    triangle.append(a)

solution(triangle)