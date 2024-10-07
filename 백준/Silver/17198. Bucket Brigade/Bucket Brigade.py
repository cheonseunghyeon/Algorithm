def find_positions(farm):
    positions = {'B': None, 'R': None, 'L': None}
    for i in range(10):
        for j in range(10):
            if farm[i][j] in positions:
                positions[farm[i][j]] = (i, j)
    return positions['B'], positions['R'], positions['L']

def calculate_distance(barn, rock, lake):
    bx, by = barn
    rx, ry = rock
    lx, ly = lake

    ans = abs(bx - lx) + abs(by - ly) - 1  # 기본 거리

    # 바위가 헛간과 호수 사이에 있을 경우 거리 조정
    if by == ry == ly:
        if (bx < rx < lx) or (bx > rx > lx):
            ans = abs(bx - lx) + 1

    if bx == rx == lx:
        if (by < ry < ly) or (by > ry > ly):
            ans = abs(by - ly) + 1

    return ans

def main():
    farm = [input().strip() for _ in range(10)]
    
    # 헛간, 바위, 호수의 위치 찾기
    barn, rock, lake = find_positions(farm)
    
    # 거리 계산
    ans = calculate_distance(barn, rock, lake)

    print(ans)

if __name__ == "__main__":
    main()
