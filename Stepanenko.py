def bubble_sort(arr):
    """
    Сортування бульбашкою
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    Сортування вибором
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """
    Сортування вставкою
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Тест
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Оригінальний масив:", test_array)

    bubble_result = bubble_sort(test_array.copy())
    print("Бульбашкове сортування:", bubble_result)

    selection_result = selection_sort(test_array.copy())
    print("Сортування вибором:", selection_result)

    insertion_result = insertion_sort(test_array.copy())
    print("Сортування вставкою:", insertion_result)