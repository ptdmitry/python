# Реализовать алгоритм пирамидальной сортировки (сортировка кучей)

def sort(array):
    start = (len(array) - 2) // 2
    while start >= 0:
        heapify(array, len(array), start)
        start -= 1
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


def heapify(array, heap_size, root_index):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    if left_child < heap_size and array[left_child] > array[root_index]:
        largest = left_child

    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)

array_lst = [9, 5, 21, 4, 0, 14, 7, 32, 15, 2, 8]
sort(array_lst)
print(f'Отсортированный массив: {array_lst}')
