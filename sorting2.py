import random
import json
import os
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

# Step 1: Create array and write to JSON file
def create_and_write_array(size_mb):
    size_bytes = size_mb * 1024 * 1024
    num_elements = size_bytes // 4  # Assuming 4 bytes per integer
    arr = [random.randint(1, 1000) for _ in range(num_elements)]
    
    with open('10mb.json', 'w') as f:
        json.dump(arr, f)
    
    return arr

# Step 2: Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in tqdm(range(n), desc="Bubble Sort"):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in tqdm(range(n), desc="Selection Sort"):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def merge_sort_with_progress(arr):
    total_operations = len(arr) * (len(arr).bit_length() - 1)
    with tqdm(total=total_operations, desc="Merge Sort") as pbar:
        def merge_sort_helper(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]

                merge_sort_helper(L)
                merge_sort_helper(R)

                i = j = k = 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                    pbar.update(1)

                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                    pbar.update(1)

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
                    pbar.update(1)

        merge_sort_helper(arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def quick_sort_with_progress(arr):
    total_operations = len(arr) * (len(arr).bit_length() - 1)
    with tqdm(total=total_operations, desc="Quick Sort") as pbar:
        def quick_sort_helper(arr):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[len(arr) // 2]
                left = [x for x in arr if x < pivot]
                middle = [x for x in arr if x == pivot]
                right = [x for x in arr if x > pivot]
                pbar.update(len(arr))
                return quick_sort_helper(left) + middle + quick_sort_helper(right)
        
        return quick_sort_helper(arr)

# Main execution
if __name__ == "__main__":
    size_mb = int(input("Enter the size of the array in MB: "))
    arr = create_and_write_array(size_mb)
    
    sorting_algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Merge Sort", merge_sort_with_progress),
        ("Quick Sort", quick_sort_with_progress)
    ]
    
    results = []
    
    for name, algo in sorting_algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        algo(arr_copy)
        end_time = time.time()
        sorting_time = end_time - start_time
        results.append((name, sorting_time))
        print(f"{name} took {sorting_time:.2f} seconds")
    
    # Plotting the results
    names, times = zip(*results)
    plt.figure(figsize=(10, 5))
    plt.bar(names, times)
    plt.title("Sorting Algorithm Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (seconds)")
    plt.show()
    
    # Conclusion
    fastest = min(results, key=lambda x: x[1])
    slowest = max(results, key=lambda x: x[1])
    
    print(f"\nConclusion:")
    print(f"The fastest algorithm was {fastest[0]} with a time of {fastest[1]:.2f} seconds.")
    print(f"The slowest algorithm was {slowest[0]} with a time of {slowest[1]:.2f} seconds.")