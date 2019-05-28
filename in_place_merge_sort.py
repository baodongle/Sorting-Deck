#!/usr/bin/env python3
"""Implement an in-place version of merge sort."""
from sorting_deck import do_bubble_sort, do_insertion_sort, do_quick_sort
from functions import parse_arguments, remove_and_insert_right_to_left


def in_place_merge(unordered_list):
    """Implement in-place Merge Sort.

    Time Complexity is O(n^2 log n) because merge is O(n^2).
    """
    my_list = unordered_list

    def merge(a_list, start, start2, end):
        while start < start2 <= end:
            # Compare the elements at which the pointers are present.
            if a_list[start] > a_list[start2]:
                # Place element2 in its right position:
                remove_and_insert_right_to_left(a_list, start, start2)
                print(*a_list)
                start2 += 1
            # Element1 is at right position
            start += 1

    def build_sorted_list(a_list, start, mid, end):
        start2 = mid + 1
        if a_list[mid] > a_list[start2]:
            merge(a_list, start, start2, end)

    def sort(a_list, left, right):
        if left < right:
            mid = left + (right - left) // 2

            # Sort first and second halves
            sort(a_list, left, mid)
            sort(a_list, mid + 1, right)

            build_sorted_list(a_list, left, mid, right)

    sort(my_list, 0, len(my_list) - 1)
    return my_list


def choose_algorithm(algo):
    """Execute sorting algorithm depending on the option --algo."""
    switcher = {
        'bubble': do_bubble_sort,
        'insert': do_insertion_sort,
        'quick': do_quick_sort,
        'merge': in_place_merge,
    }
    return switcher[algo]


if __name__ == "__main__":
    args = parse_arguments()
    series = args.integers
    if len(series) > 15 and args.gui:
        print("Input too large")
    else:
        choose_algorithm(args.algo)(series)
