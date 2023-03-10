# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        while left < n:
            if data[left] < data[min_index]:
                min_index = left
            if right < n and data[right] < data[min_index]:
                min_index = right
            if i != min_index:
                swaps.append((i, min_index))
                data[i], data[min_index] = data[min_index], data[i]
                i = min_index
                left = 2 * i + 1
                right = 2 * i + 2
            else:
                break
    return swaps


def main():
    text = input()
    if 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in text:
        name = input()
        if not 'a' in name: 
            name = "tests/"+name
            f = open(name, "r")
            n = int(f.readline())
            data = list(map(int,f.readline().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
