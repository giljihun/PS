n = int(input())

# 주어진 수열을 저장하는 변수 'data'
data = list(map(int, input().split()))

# 숫자가 1개만 주어지면 뒤에 올 수는 모든 숫자가 가능함.
if n == 1:
    print('A')

# 숫자가 2개만 주어졌을 때, 두 숫자가 같으면 다음 숫자는 무조건 같음.
elif n == 2:
    if data[0] == data[1]:
        print(data[0])
    # 숫자가 2개만 주어졌을 때, 두 숫자가 다르다면 뒤에 올 수는 뭐가 나올 지 모른다.
    else:
        print('A')
# 숫자가 3개 이상 주어졌을 때.
else:
    # 기울기의 분모가 0이 되버리는 경우 예외처리.
    if data[0] == data[1]:
        a = 0
    else:
        # 기울기 구하는 식.
        a = (data[2] - data[1]) // (data[1] - data[0])

    # y절편 구하는 식.
    b = data[1] - data[0] * a

    # a와 b를 통해 예측값과 실제값을 비교. 만약 틀리다면 구할 수 없는 경우
    for i in range(n - 1):
        # 다음 예측값
        expect = data[i] * a + b
        # 예측값과 실제가 다르다면
        if (data[i + 1] != expect):
            print('B')
            exit()

    # 예측값과 실제값이 모두 같다면, 다음 예측 값을 구함. data[-1]은 data 리스트의 가장 마지막 값을 의미
    print(data[-1] * a + b)