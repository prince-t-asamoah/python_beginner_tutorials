import statistics, random

def quicksort(numbers: list[int]):
    """Simple quick sort implementation for sorting a list of numbers"""
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot ]
        )
        return (quicksort(items_less) + pivot_items + quicksort(items_greater))

def bubble_sort(numbers: list[int]):
    """Simple bubble sort implementation for sorting a list of numbers"""
    for number in range(len(numbers) - 1, 0, -1):
        swapped =  False
        
        for i in range(number):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        if not swapped:
            break


def get_random_numbers(length, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))
    return numbers
    
print(quicksort([]))
print(quicksort([42]))
print(quicksort([5, 2, 6, 3]))
print(quicksort([10, -3, 21, 6, -8]))


# Test with random numbers
numbers = get_random_numbers(20)
print('Quicksort: ', quicksort(numbers))

numbers = get_random_numbers(15, -50, 50)
print('Quicksort: ', quicksort(numbers))


numbers = get_random_numbers(20)
print('Bubble sort: ', quicksort(numbers))

numbers = get_random_numbers(15, -50, 50)
print('Bubble sort: ', quicksort(numbers))

