import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def nearest_insertion(points):
    n = len(points)
    unvisited = set(range(n))
    current_point = 0
    tour = [current_point]

    while unvisited:
        nearest_point = min(unvisited, key=lambda p: distance(points[current_point], points[p]))
        min_distance = distance(points[current_point], points[nearest_point])
        insert_index = None
        
        for i in range(len(tour)):
            p1 = tour[i]
            p2 = tour[(i+1) % len(tour)]
            dist = distance(points[p1], points[nearest_point]) + distance(points[nearest_point], points[p2]) - distance(points[p1], points[p2])
            if insert_index is None or dist < min_distance:
                insert_index = i + 1
                min_distance = dist
        
        tour.insert(insert_index, nearest_point)
        unvisited.remove(nearest_point)
        current_point = nearest_point

    return tour

def main():
    points = [
        (-17.39257930,	18.63281250),   # 첫 번째 웨이 포인트의 위도, 경도
        (12.21118020,	28.47656250),   # 두 번째 웨이 포인트의 위도, 경도
        (-1.31824310,	32.16796880),   # 세 번째 웨이 포인트의 위도, 경도
        (7.36246690,    15.11718750),   # 네 번째 웨이 포인트의 위도, 경도
        (-9.70905710,	28.91601560),   # 다섯 번째 웨이 포인트의 위도, 경도
        (-2.72358310,	13.44726560)    # 여섯 번째 웨이 포인트의 위도, 경도
    ]

    tour = nearest_insertion(points)
    print("순서:", tour)
    print("경로:", [points[i] for i in tour])

if __name__ == "__main__":
    main()
