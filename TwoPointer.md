## 투 포인터 알고리즘



### 1. 개념

배열이나 리스트와 같은 순차적인 자료구조에서 특정 범위 내에서 원하는 값을 찾거나 구하는 알고리즘 기법!

### 2. 원리

- 보통 왼쪽 포인터와 오른쪽 포인터 두 개의 포인터 변수를 사용한다. 이 두 포인터 변수를 이용하여 원하는 범위 내에서 값을 찾을 수 있다!

### 3. 예시 & Code

ex - [주어진 배열에서 합이 특정한 값을 가지는 부분 배열을 찾아라]

````python
def find_subarray_sum(arr, target_sum):
  left, right = 0, 0
  current_sum = arr[0]
  n = len(arr)
  while left < n and right < n:
    if current_sum == target_sum:
      return left, right
    elif current_sum < target_sum:
      right += 1
      if right < n:
        current_sum += arr[right]
      else:
        current_sum -= arr[left]
        left += 1
  return None
````

1. 배열 'arr'과 찾고자 하는 부분 배열의 합 'target_sum'을 입력값으로 받는다.
2. 왼쪽 포인터 'left'와 오른쪽 포인터 'right'를 0으로 초기화한다.
3. 'current_sum' 변수를 배열의 첫 번째 요소 'arr[0]'로 초기화한다.
4. While 조건에 따라 아래의 과정을 반복한다.
   - 'current_sum'이 'target_sum'과 같다면, 현재의 부분 배열의 합이 'target_sum'과 같으므로 이 부분 배열을 반환한다.
   - 'current_sum'이 'target_sum'보다 작다면, 'right' 포인터를 오른쪽으로 이동시키고, 'current_sum'에 'arr[right]' 값을 더해준다.
   - 'current_sum'이 'target_sum'보다 크다면, 'left' 포인터를 오른쪽으로 이동시키고, 'current_sum'에서 'arr[left]' 값을 빼준다.
5. 위 과정을 반복하면서 'target_sum'과 같은 부분 배열을 찾지 못하면 'None'을 반환한다.
6. 예를 들어, 입력값으로 `arr = [1, 4, 20, 3, 10, 5], target_sum = 33`을 주면, 함수는 `(2, 4)`를 반환합니다. 이는 배열 `arr`에서 세 번째부터 다섯 번째 요소까지의 부분 배열 `[20, 3, 10]`의 합이 33이기 때문입니다.
