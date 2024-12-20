def bubble_sort(data: list[int]) -> list[int]:
    print(f"Data before sorting: {data}")
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(i, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def do_operations(data: list[int]) -> None:
    # multiply each element by 2 and add 10
    for i in range(len(data)):
        data[i] = data[i] * 2 + 10

    result = bubble_sort(data)

    print(f"Result after sorting: {result}")


def main() -> None:
    data = [1, 5, 3, 4, 2]
    do_operations(data)


if __name__ == "__main__":
    main()
