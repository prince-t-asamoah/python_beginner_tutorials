def count_leaf_items_recursive(item_list: list):
    """
    Recursively counts and returns the number of leaf
    items in a (potentially nested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print('Encountered sublist')
            count += count_leaf_items_recursive(item)
        else:
            print(f"Counted leaf item '{item}'")
            count += 1
    print(f"-> Returning count {count}")
    return count

def count_leaf_items_non_recursive(item_list: list):
    """
        Non-recursively coounts and returns the number
        of leaf items in a (potentially nested) list.
    """
    count = 0
    i = 0
    stack = []
    current_list = item_list
    
    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
        else:
            current_list, i = stack.pop()
            i += 1
            continue
        
        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1
        
names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert",
    ],
    "Alex",
    ["Bea", "Bill"],
    "Ann",
]


print('Recursive: ', count_leaf_items_recursive([1, 2, 3, 4]))
print('Recursive: ', count_leaf_items_recursive([1, [.1, 2.2], 3]))
print('Recursive: ', count_leaf_items_recursive([]))
print('Recursive: ', count_leaf_items_recursive(names))

print('Non-recursive: ', count_leaf_items_non_recursive([1, 2, 3, 4]))
print('Non-recursive: ', count_leaf_items_non_recursive([1, [.1, 2.2], 3]))
print('Non-recursive: ', count_leaf_items_non_recursive([]))
print('Non-recursive: ', count_leaf_items_non_recursive(names))
