def calculate_positive_average(numbers):
    """
    Вычисляет среднее арифметическое положительных элементов в списке `numbers`.
    Возвращает 0, если положительных элементов нет.
    """
    total = 0
    count = 0
    for el in numbers:
        if el > 0:
            total += el
            count += 1
    if count > 0:
        average = total / count  # Строка A
    else:
        average = 0
    return average

nums = [1,2,3]
print(calculate_positive_average(nums))
