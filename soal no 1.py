
import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time
    return arr, execution_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time
    return arr, execution_time


def print_iterations(arr):
    print("Iterasi pertama:")
    print(arr[:5])
    print("Iterasi terakhir:")
    print(arr[-5:])
    print()


def print_sorted(arr):
    print("Sebelum pengurutan:")
    print(numbers)
    print("Setelah pengurutan:")
    print(arr)
    print()


def worst_case(arr):
    n = len(arr)
    return (n - 1) * (n - 1)


def best_case(arr):
    return 0


def average_case(arr):
    n = len(arr)
    return (n - 1) * (n - 1) // 2

user_choice = input("Pilih metode pengurutan (bubble sort / insertion sort): ")
numbers = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

if user_choice.lower() == 'bubble sort':
    sorted_numbers, execution_time = bubble_sort(numbers.copy())
    print_iterations(sorted_numbers)
    print_sorted(sorted_numbers)
    print("Waktu komputasi:", execution_time, "detik")
    print("Worst case:", worst_case(numbers))
    print("Best case:", best_case(numbers))
    print("Average case:", average_case(numbers))
elif user_choice.lower() == 'insertion sort':
    sorted_numbers, execution_time = insertion_sort(numbers.copy())
    print_iterations(sorted_numbers)
    print_sorted(sorted_numbers)
    print("Waktu komputasi:", execution_time, "detik")
    print("Worst case:", worst_case(numbers))
    print("Best case:", best_case(numbers))
    print("Average case:", average_case(numbers))
else:
    print("Pilihan tidak valid.")
