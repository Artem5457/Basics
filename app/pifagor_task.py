def pifagor_pants(sizes: list[int]) -> bool:
    squared_sizes = [size ** 2 for size in sizes]
    squared_sizes.sort()

    if len(squared_sizes) == 3:
        a, b, c = squared_sizes
        return c == a + b

    return False
