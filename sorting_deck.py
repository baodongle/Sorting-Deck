#!/usr/bin/env python3
"""Implement different sorting algorithms and to visualise those algorithms."""
from functions import (swap_elements, copy_elements, parse_arguments,
                       remove_and_insert_right_to_left)


def do_bubble_sort(unordered_list):
    """Implement of Bubble Sort.

    Time Complexity of Bubble Sort:
        - Best Case is O(n): If the list is already sorted.
        - Average Case is O(n^2)
        - Worst Case is O(n^2): If the list is sorted in reverse order.
    """
    my_list = unordered_list

    def compare_pairs(a_list, last_swap):
        swapped = False
        for i in range(last_swap):
            # Check the adjacent elements:
            if a_list[i] > a_list[i + 1]:
                swap_elements(a_list, i, i + 1)
                print(*my_list)
                swapped = True
                last_swap = i
        # All elements after the last swap are sorted
        return swapped, last_swap

    def sort(a_list):
        last_swap = len(a_list) - 1
        for _ in range(1, len(a_list)):
            swapped, last_swap = compare_pairs(a_list, last_swap)
            # No swapping happened, the list is sorted:
            if not swapped:
                break

    sort(my_list)
    return my_list


def do_insertion_sort(unordered_list):
    """Implement Insertion Sort.

    Time Complexity of Insertion Sort:
        - Best Case is O(n): If the list is already sorted.
        - Average Case is O(n^2).
        - Worst Case is O(n^2): If the list is sorted in reverse order.
    """
    my_list = unordered_list

    def do_insert(a_list, pos):
        for i in range(pos):
            if a_list[pos] < a_list[i]:
                remove_and_insert_right_to_left(a_list, i, pos)
                print(*a_list)
                return

    def sort(a_list):
        for i in range(1, len(a_list)):
            if a_list[i] >= a_list[i - 1]:  # ordered
                continue
            do_insert(a_list, i)

    sort(my_list)
    return my_list


def do_quick_sort(unordered_list):
    """Implement Quick Sort.

    Time Complexity of Quick Sort:
        - Best Case is O(n log n): Each time perform a partition will divide
        the list into two nearly equal pieces.
        - Average Case is O(n log n).
        - Worst Case is O(n^2): If the pivot happens to be the smallest or
        largest element in the list.
    """
    my_list = unordered_list

    def partition(a_list, low, high):
        """Partitioning: reorder the list.

        1. Takes last element as pivot.
        2. Place the pivot element at its correct position in sorted list.
        3. Place all smaller (than pivot) to left of pivot and all greater
        to right of pivot.
        """
        pivot = a_list[high]
        print("P:", pivot)
        i = low - 1  # index of smaller element
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if a_list[j] <= pivot:
                i += 1  # increase index of smaller element
                swap_elements(a_list, i, j)

        swap_elements(a_list, i + 1, high)
        print(*a_list)
        return i + 1

    def sort(a_list, low, high):
        while low < high:
            # Get partitioning index:
            index = partition(a_list, low, high)
            # a_list[pi] is now at right place

            # If left part is smaller:
            if index - low < high - index:
                # Recur for left part and handle right part interatively
                sort(a_list, low, index - 1)
                low = index + 1
            else:
                # Recur for right part
                sort(a_list, index + 1, high)
                high = index - 1

    sort(my_list, 0, len(my_list) - 1)
    return my_list


def do_merge_sort(unordered_list):
    """Implement Merge Sort.

    Time Complexity of Quick Sort: O(n log n).
    """
    my_list = unordered_list

    def merge_sublists(merged_list, first, second):
        # Initialize 3 pointers of 2 sub-lists (i, j) and the merged list (k):
        i, j, k = 0, 0, 0

        # Copy smaller element into sorted list:
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                merged_list[k] = first[i]
                i += 1
            else:
                merged_list[k] = second[j]
                j += 1
            k += 1
        return i, j, k

    def build_sorted_list(a_list, left, right):
        i, j, k = merge_sublists(a_list, left, right)
        # Reached the end of one of the sub-lists:
        copy_elements(left, a_list, i, k)
        copy_elements(right, a_list, j, k)

    def sort(a_list):
        if len(a_list) > 1:
            mid = len(a_list) // 2
            # Dividing the list into 2 halves
            left = a_list[:mid]
            right = a_list[mid:]

            sort(left)  # Sorting the first half
            sort(right)  # Sorting the second half

            build_sorted_list(a_list, left, right)
            print(*a_list)

    sort(my_list)
    return my_list


def choose_algorithm(algo):
    """Chosse sorting algorithm depending on the option --algo."""
    switcher = {
        'bubble': do_bubble_sort,
        'insert': do_insertion_sort,
        'quick': do_quick_sort,
        'merge': do_merge_sort,
    }
    return switcher[algo]


if __name__ == "__main__":
    args = parse_arguments()
    series = args.integers
    if len(series) > 15 and args.gui:
        print("Input too large")
    else:
        choose_algorithm(args.algo)(series)
