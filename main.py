import random
import pandas as pd

# Liczniki operacji porównania i podstawienia
comparison_counter = 0
swap_counter = 0

def reset_counters():
    global comparison_counter, swap_counter
    comparison_counter = 0
    swap_counter = 0

def selection_sort(arr):
    global comparison_counter, swap_counter
    reset_counters()
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparison_counter += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swap_counter += 1

def bubble_sort(arr):
    global comparison_counter, swap_counter
    reset_counters()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparison_counter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_counter += 1

def bubble_sort_flag(arr):
    global comparison_counter, swap_counter
    reset_counters()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparison_counter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_counter += 1
                swapped = True
        if not swapped:
            break

def insertion_sort(arr):
    global comparison_counter, swap_counter
    reset_counters()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparison_counter += 1
            arr[j + 1] = arr[j]
            swap_counter += 1
            j -= 1
        arr[j + 1] = key

def run_experiment(data_generator, method_names, display_progress=True):
    sizes = list(range(1000, 100001, 1000))
    results = {"Data Size": sizes}

    for method_name in method_names:
        comparison_results = []
        swap_results = []
        for size in sizes:
            data = data_generator(size)
            eval(method_name)(data.copy())
            comparison_results.append(comparison_counter)
            swap_results.append(swap_counter)

            # Wyświetlanie postępu po każdych 1000 sortowaniach
            if display_progress and size % 1000 == 0:
                print(f"Method: {method_name}, Data Size: {size}, Comparisons: {comparison_counter}, Swaps: {swap_counter}")

        results[f"{method_name}_comparisons"] = comparison_results
        results[f"{method_name}_swaps"] = swap_results

    return results

def random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def ascending_data(size):
    return list(range(1, size + 1))

def descending_data(size):
    return list(range(size, 0, -1))

def save_to_excel(results, filename):
    df = pd.DataFrame(results)
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    method_names = ["selection_sort", "bubble_sort", "optimized_bubble_sort", "insertion_sort"]

    random_results = run_experiment(random_data, method_names)
    ascending_results = run_experiment(ascending_data, method_names)
    descending_results = run_experiment(descending_data, method_names)

    save_to_excel(random_results, "random_results_operations.xlsx")
    save_to_excel(ascending_results, "ascending_results_operations.xlsx")
    save_to_excel(descending_results, "descending_results_operations.xlsx")

    print("Results saved to Excel files.")