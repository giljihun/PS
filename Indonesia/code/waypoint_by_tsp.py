import math
import argparse
# 두 점 사이의 거리를 계산


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# TSP(Traveling Salesman Problem, 여행자 문제!)를 해결하기 위한
# (TSP는 여러 도시들을 방문하고 다시 시작 도시로 돌아오는 가장 짧은 경로를 찾는 문제입니다.)
# 근사 알고리즘 중 하나인 "최근 삽입 알고리즘"으로
# 최근 삽입 알고리즘은 TSP 문제에서 여행 경로를 생성하는 방법 중 하나이며
# 초기 경로를 하나의 점으로 시작하여 각 단계에서 가장 가까운 점을 경로에 추가해 나가는 방식입니다.


def nearest_insertion(points):
    n = len(points)  # 입력된 점들의 수
    unvisited = set(range(n))  # 초기에 아직 방문하지 않은 모든 점 집합
    current_point = 0  # 시작점 -> 당연히 첫번째 점!
    tour = [current_point]  # 우리가 얻을 경로를 나타내는 리스트

    # 방문하지 않은 점들이 있다면 반복
    while unvisited:
        # 현재 점에서 가장 가까운 점 선택
        nearest_point = min(unvisited, key=lambda p: distance(
            points[current_point], points[p]))

        # 현재 점과 가장 가까운 점 사이의 거리를 계산
        min_distance = distance(points[current_point], points[nearest_point])

        # 삽입할 위치를 나타내는 변수를 초기화
        insert_index = None

        # 경로의 각 위치에 대해 최적 위치를 찾음
        for i in range(len(tour)):
            # 현재 위치를 p1으로 설정
            p1 = tour[i]
            # 다음 위치의 점을 p2로 설정
            p2 = tour[(i+1) % len(tour)]

            # 최적 위치에 대한 거리를 계산하고, 더 작은 거리를 찾으면 insert_index, min_distance를 업데이트.
            dist = distance(points[p1], points[nearest_point]) + distance(
                points[nearest_point], points[p2]) - distance(points[p1], points[p2])
            if insert_index is None or dist < min_distance:
                insert_index = i + 1
                min_distance = dist
        # 최적 위치에 가장 가까운 점을 삽입
        tour.insert(insert_index, nearest_point)
        # 방문한 점을 'unvisted'에서 제거
        unvisited.remove(nearest_point)
        # 현재 점을 가장 가까운 점으로 업데이트
        current_point = nearest_point

    # 최종 위치 반환
    return tour


def main():
    parser = argparse.ArgumentParser(description="Adjust Waypoints with TSP")
    parser.add_argument("input_file", help="Input waypoints file")
    parser.add_argument("output_file", help="Output waypoints file")

    args = parser.parse_args()
    
    with open(args.input_file, "r") as file:
        lines = file.readlines()

    # 맨 위 두줄은 위도, 경도 데이터가 아닌 칼럼이므로 제외합니다.
    data_lines = [line.strip().split("\t")
                  for line in lines[2:]]

    # 줄 별 위도 경도값 리스트화
    latitudes = [float(row[8]) for row in data_lines]
    longitudes = [float(row[9]) for row in data_lines]

    points = list(zip(latitudes, longitudes))
    tour = nearest_insertion(points)

    # [0, 9, 6, 1, 5, 4, 7, 8, 2, 3] 이런식으로 순서가 출력됨.
    print(points)

    with open(new_file_name, "w") as new_file:
        # waypoints 파일의 1,2번 줄은 무슨 내용인진 몰겠지만
        # 없으면 파일 불러오기 안될거같으니 각각 항상 추가
        new_file.write(lines[0])
        new_file.write(lines[1])
        tour.pop()
        print(tour)
        index = 1

        # 획득한 경로 순서를 토대로 데이터 입력
        for i in tour:
            lat, lon = points[i]
            line = f"{index}\t{data_lines[i][1]}\t{data_lines[i][2]}\t{data_lines[i][3]}\t{data_lines[i][4]}\t{data_lines[i][5]}\t{data_lines[i][6]}\t{data_lines[i][7]}\t{lat:.8f}\t{lon:.8f}\t{data_lines[i][10]}\t{data_lines[i][11]}\n"
            new_file.write(line)
            index += 1


if __name__ == "__main__":
    main()
