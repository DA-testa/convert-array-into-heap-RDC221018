# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and data[left] < data[min_index]:
            min_index = left
        if right < n and data[right] < data[min_index]:
            min_index = right
        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            j_swaps = build_heap(data)
            swaps.extend(j_swaps)
    return swaps

def main():
    text = input()
    if "I" in (text):
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    elif "F" in text:
        filename = input()
        if not 'a' in filename:
            filename = "tests/" + filename
            f = open(filename, "r")
            n = f.readline()
            n = int(n)
            data = f.readline()
            data = list(map(int, data.split()))
            assert len(data) == n
            swaps = build_heap(data)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)
    pass



if __name__ == "__main__":
    main()
