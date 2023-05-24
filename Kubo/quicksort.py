import sys
args = sys.argv


def quicksort(array):
    '''クイックソートを行う関数'''

    # 長さが1未満の場合はarrayを返す
    if len(array) < 1:
        return array

    # point = 基準
    # left = pointより小さい値を格納するlist
    # right = pointより大きい値を格納するlist
    point = array[0]
    left, right = [], []
    # 1から配列の長さまで繰り返し
    for i in range(1, len(array)):
        # 基準より値が小さい場合leftに格納
        if point >= array[i]:
            left.append(array[i])
        # 基準より値が大きい場合rightに格納
        elif point <= array[i]:
            right.append(array[i])

    # left、rightの中身を再帰的にソート
    left = quicksort(left)
    right = quicksort(right)

    # leftの最後に基準を追加
    left.append(point)
    # leftとrightを繋げたものを返す
    return left + right


array = list(map(int, args[1:]))
print(f"整理前：{array}")
array = quicksort(array)
print(f"整理後：{array}")
