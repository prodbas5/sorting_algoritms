# Sorting Algorithm Comparison

This project demonstrates the implementation and comparison of various sorting algorithms in Python. It creates an array of random integers, saves it to a JSON file, sorts the array using different algorithms, and compares their performance.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Algorithms](#algorithms)
5. [Implementation Details](#implementation-details)
6. [Performance Comparison](#performance-comparison)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

1. Ensure you have Python 3.6+ installed on your system.
2. Clone this repository:
git clone https://github.com/prodbas5/sorting-algorithm-comparison.git
cd sorting-algorithm-comparison
Copy3. Install the required dependencies:
pip install tqdm matplotlib
Copy
## Usage

Run the script using Python:
python sort_comparison.py
Copy
When prompted, enter the desired size of the array in megabytes (MB).

## Features

- Creates an array of random integers based on user-specified size
- Saves the array to a JSON file
- Implements and compares four sorting algorithms:
  - Bubble Sort (slow)
  - Selection Sort (slow)
  - Merge Sort (fast)
  - Quick Sort (fast)
- Displays progress bars for each sorting algorithm
- Calculates and compares sorting times
- Generates a bar graph to visualize performance differences
- Provides a conclusion about the fastest and slowest algorithms

## Algorithms

### Bubble Sort

- **Time Complexity**: O(n^2)
- **Space Complexity**: O(1)
- **Description**: Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

### Selection Sort

- **Time Complexity**: O(n^2)
- **Space Complexity**: O(1)
- **Description**: Divides the input list into two parts: a sorted portion at the left end and an unsorted portion at the right end. Repeatedly selects the smallest element from the unsorted portion and moves it to the sorted portion.

### Merge Sort

- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Description**: Divides the unsorted list into n sublists, each containing one element, then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

### Quick Sort

- **Time Complexity**: O(n log n) average case, O(n^2) worst case
- **Space Complexity**: O(log n)
- **Description**: Picks an element as a pivot and partitions the array around the pivot. The pivot is positioned in its final sorted position, with smaller elements to the left and larger elements to the right.

## Implementation Details

### Array Creation and File Writing

- The `create_and_write_array` function generates an array of random integers between 1 and 1000.
- The size of the array is determined by the user input in megabytes (MB).
- The array is then written to a JSON file named '10mb.json' in the current directory.

### Sorting Algorithms

- Each sorting algorithm is implemented as a separate function.
- Progress bars are added using the `tqdm` library to visualize the sorting process.
- For Merge Sort and Quick Sort, recursive helper functions are used to implement the progress bar correctly.

### Performance Measurement

- The script measures the execution time of each sorting algorithm using the `time` module.
- Results are stored and later used for comparison and visualization.

### Visualization

- A bar graph is generated using `matplotlib` to compare the sorting times of all algorithms.
- The x-axis represents the sorting algorithms, and the y-axis represents the time taken in seconds.

## Performance Comparison

The script provides a visual and textual comparison of the sorting algorithms:

1. A bar graph showing the time taken by each algorithm.
2. A printed conclusion stating the fastest and slowest algorithms with their respective times.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).
