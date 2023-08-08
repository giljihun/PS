import tkinter as tk
from tkinter import filedialog
import os
import math

# 두 점 사이의 거리를 계산하는 함수
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


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

# 파일 선택 대화상자를 열어 입력 파일 선택
def browse_input_file():
    input_file_path = filedialog.askopenfilename(filetypes=[("Waypoints Files", "*.waypoints")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file_path)

# 파일 선택 대화상자를 열어 출력 파일 선택
def browse_output_file():
    output_file_path = filedialog.asksaveasfilename(defaultextension=".waypoints",
                                                    filetypes=[("Waypoints Files", "*.waypoints")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file_path)


# 변환 시작 함수
def start_conversion():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()

    # 입력 파일이나 출력 파일 이름이 비어있는 경우 에러 메시지 표시
    if not input_file or not output_file:
        result_label.config(text="Please specify input and output files.")
        return

    # 입력 파일 읽기
    with open(input_file, "r") as file:
        lines = file.readlines()
    data_lines = [line.strip().split("\t")
                  for line in lines[2:]]
    latitudes = [float(row[8]) for row in data_lines]
    longitudes = [float(row[9]) for row in data_lines]
    points = list(zip(latitudes, longitudes))
    tour = nearest_insertion(points)
    # 출력 파일에 결과 저장
    with open(output_file, "w") as new_file:
        new_file.write(lines[0])
        new_file.write(lines[1])
        tour.pop()
        index = 1
        for i in tour:
            lat, lon = points[i]
            line = f"{index}\t{data_lines[i][1]}\t{data_lines[i][2]}\t{data_lines[i][3]}\t{data_lines[i][4]}\t{data_lines[i][5]}\t{data_lines[i][6]}\t{data_lines[i][7]}\t{lat:.8f}\t{lon:.8f}\t{data_lines[i][10]}\t{data_lines[i][11]}\n"
            new_file.write(line)
            index += 1
    result_label.config(text="Conversion completed.")

    # 파일 변환 코드 실행
    # 경로 조정 후 출력 파일에 저장

    result_label.config(text="I Love TelKom Univ..")

# GUI 창 생성
root = tk.Tk()
root.title("Waypoints Conversion")

# 입력 파일 선택
input_label = tk.Label(root, text="Input File:")
input_label.pack()
input_file_entry = tk.Entry(root)
input_file_entry.pack()
browse_input_button = tk.Button(root, text="Browse", command=browse_input_file)
browse_input_button.pack()

# 출력 파일 선택
output_label = tk.Label(root, text="Output File:")
output_label.pack()
output_file_entry = tk.Entry(root)
output_file_entry.pack()

# 변환 시작 버튼
start_button = tk.Button(root, text="Applying the Algorithm", command=start_conversion)
start_button.pack()

# 변환 결과 표시 레이블
result_label = tk.Label(root, text="")
result_label.pack()

# GUI 실행
root.mainloop()
