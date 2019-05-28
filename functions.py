"""Make some useful functions for the main program."""
from argparse import ArgumentParser


def parse_arguments():
    """Command line option and argument parsing."""
    parser = ArgumentParser()
    parser.add_argument(
        '--algo',
        default='bubble',
        metavar='ALGO',
        choices=['bubble', 'insert', 'quick', 'merge'],
        help='''specify which algorithm to use for sorting
                        among [bubble|insert|quick|merge], default bubble''')
    parser.add_argument(
        '--gui',
        action='store_true',
        help='''visualise the algorithm in GUI mode''')
    parser.add_argument(
        'integers',
        metavar='N',
        type=int,
        nargs='+',
        help='an integer for the list to sort')
    args = parser.parse_args()
    return args


def swap_elements(a_list, pos1, pos2):
    """Swap elements at given postions."""
    a_list[pos1], a_list[pos2] = a_list[pos2], a_list[pos1]
    return a_list


def copy_elements(first_list, second_list, pos1, pos2):
    """Copy remaining elements from first_list to second_list."""
    while pos1 < len(first_list):
        second_list[pos2] = first_list[pos1]
        pos1 += 1
        pos2 += 1


def remove_and_insert_right_to_left(a_list, left, right):
    """Remove the element in the right and insert to the left."""
    tmp = a_list[right]
    a_list[left + 1:right + 1] = a_list[left:right]
    a_list[left] = tmp
