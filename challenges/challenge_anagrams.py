def quick_sort(letters, start, end):
    if start < end:
        part = partition(letters, start, end)
        quick_sort(letters, start, part - 1)
        quick_sort(letters, part + 1, end)


def partition(letters, start, end):
    pivot = letters[end]
    delimiter = start - 1

    for index in range(start, end):
        if letters[index] <= pivot:
            delimiter += 1
            letters[index], letters[delimiter] = (
                letters[delimiter],
                letters[index],
            )

    letters[delimiter + 1], letters[end] = letters[end], letters[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return False

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    quick_sort(first_list, 0, len(first_list) - 1)
    quick_sort(second_list, 0, len(second_list) - 1)

    first_sorted = "".join(first_list)
    second_sorted = "".join(second_list)

    if not len(first_sorted) or not len(second_sorted):
        return (first_sorted, second_sorted, False)

    is_valid = first_sorted == second_sorted

    return (first_sorted, second_sorted, is_valid)
