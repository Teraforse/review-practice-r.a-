def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True  # 0 и 1 — квадраты

    low = 2
    high = n // 2  # Оптимизация

    while low <= high:
        mid = (low + high) // 2
        mid_sq = mid * mid

        if mid_sq == n:
            return True
        elif mid_sq < n:
            low = mid + 1
        else:
            high = mid - 1

    return False
n = int(input('Введите значение: '))
print(is_perfect_square(n))