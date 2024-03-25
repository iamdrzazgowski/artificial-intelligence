def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n-1, source, auxiliary, target)
        print(f"Przenieś dysk {n} z {source} do {target}")
        hanoi(n-1, auxiliary, target, source)

n = 3
hanoi(n, 'A', 'C', 'B')