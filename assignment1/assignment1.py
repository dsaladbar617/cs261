# Name: Daniel Salzar
# OSU Email: salazdan@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: April 22, 2024
# Description: Implementing various functions using StaticArray class.


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    This function finds the minimum and maximum values in the input array.
    """
    min = arr.get(0)
    max = arr.get(0)

    # Iterate through the StaticArray to find the minimum and maximum values
    for i in range(arr.length()):
        if arr.get(i) < min:
            min = arr.get(i)
        elif arr.get(i) > max:
            max = arr.get(i)

    return (min, max)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    This function replaces numbers in the input array with "fizz" if the number is divisible by 3, "buzz" if the number is divisible by 5, and "fizzbuzz" if the number is divisible by both 3 and 5. Otherwise, the number is returned.
    """
    new_arr = StaticArray(arr.length())
    # Iterate through the StaticArray to check if the number is divisible by 3, 5, or both.
    for i in range(arr.length()):
        if arr.get(i) % 3  == 0 and arr.get(i) % 5 == 0:
            new_arr.set(i, "fizzbuzz")
        elif arr.get(i) % 3 == 0:
            new_arr.set(i, "fizz")
        elif arr.get(i) % 5 == 0:
            new_arr.set(i, "buzz")
        else:
            new_arr.set(i, arr.get(i))

    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    This function reverses the input array in place.
    """
    # Iterate through the StaticArray to swap the first and last elements, then the second and second to last elements, etc.
    for i in range(arr.length() // 2):
        end = arr.length() - i - 1
        prev = arr.get(i)
        arr.set(i, arr.get(end))
        arr.set(end, prev)
    return

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    This function rotates the input array by the number of steps specified. positive steps rotate the array to the right, and negative steps rotate the array to the left.
    """

    new_arr = StaticArray(arr.length())

    # Iterate through the StaticArray to set the values in the new StaticArray. Using the modulo operator to wrap around the array to not throw an index out of bounds error.
    for i in range(arr.length()):
        new_arr.set((i + steps) % arr.length(), arr.get(i))

    return new_arr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    This function creates an array of integers from start to end.
    """

    # Create a StaticArray with the correct length
    arr = StaticArray(abs(end - start) + 1)

    # Iterate through the StaticArray to set the values from start to end
    for i in range(arr.length()):
        arr.set(i, start)
        if start < end:
            start += 1
        elif start > end:
            start -= 1

    return arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    This function returns 1 if the input array is sorted in ascending order, -1 if the input array is sorted in descending order, and 0 if the input array is not sorted.
    """
    ascending = True
    descending = True

    # Iterate through the StaticArray to check if the array is sorted in ascending or descending order
    for i in range(arr.length() - 1):
        if arr.get(i) >= arr.get(i + 1):
            ascending = False
        if arr.get(i) <= arr.get(i + 1):
            descending = False

    if ascending:
        return 1
    elif descending:
        return -1
    else:
        return 0




# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    This function finds the mode of the input array and returns a tuple containing the mode and its frequency.
    """

    mode = arr.get(0)
    frequency = 1
    current_element = arr.get(0)
    current_frequency = 1

    # Iterate through the StaticArray to find the mode and its frequency
    for i in range(1, arr.length()):
        if arr.get(i) == current_element:
            current_frequency += 1
        else:
            if current_frequency > frequency:
                mode = current_element
                frequency = current_frequency
            current_element = arr.get(i)
            current_frequency = 1

    if current_frequency > frequency:
        mode = current_element
        frequency = current_frequency

    return (mode, frequency)


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    This function removes duplicates from the input array and returns a new array with the duplicates removed.
    """
    total = 1
    # Iterate through the StaticArray to count the number of unique elements
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            total += 1

    new_arr = StaticArray(total)

    if arr.length() <= 1:
        new_arr.set(0, arr.get(0))

    index = 0
    new_arr.set(index, arr.get(0))

    # Iterate through the StaticArray to add the unique elements to the new StaticArray
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            index += 1
            new_arr.set(index, arr.get(i))


    return new_arr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    This function sorts the input array using the count sort algorithm.
    """
    # Set min and max values to the first element in the StaticArray
    min_val = arr.get(0)
    max_val = arr.get(0)

    # Iterate through the array to find the min and max values
    for i in range(1, arr.length()):
        if arr.get(i) < min_val:
            min_val = arr.get(i)
        elif arr.get(i) > max_val:
            max_val = arr.get(i)

    # Create a StaticArray to store the count of each element
    count = StaticArray(max_val - min_val + 1)
    for i in range(count.length()):
        count.set(i, 0)
    # Iterate through the array to count the frequency of each element
    for i in range(arr.length()):
        count.set(arr.get(i) - min_val, count.get(arr.get(i) - min_val) + 1)

    new_arr = StaticArray(arr.length())
    index = 0
    # Iterate through the count array from last to first to create the sorted array
    for i in range(count.length() - 1, -1, -1):
        while count.get(i) > 0:
            new_arr.set(index, i + min_val)
            index += 1
            count.set(i, count.get(i) - 1)

    return new_arr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    This function squares each element in the input array and returns a new array containing the squared elements in ascending order.
    """
    n = arr.length()
    result = StaticArray(n)
    # Create a pointer for the first and last elements in the StaticArray
    left = 0
    right = n - 1
    # Iterate through the array and compare the two pointers.
    for i in range(n - 1, -1, -1):
        # If the left pointer is greater than the right pointer, square the left pointer and add it to the result array and move the left pointer to the right.
        if abs(arr.get(left)) > abs(arr.get(right)):
            result.set(i, arr.get(left) ** 2)
            left += 1
        # If the right pointer is greater than the left square the right pointer and add it to the result array and move the right pointer to the left.
        else:
            result.set(i, arr.get(right) ** 2)
            right -= 1
    return result

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
