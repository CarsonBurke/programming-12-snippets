import sys

""" 
- For every element of the list do a pass
- For each pass, take index i -> list length - 1 as j and record i in the sorted list as the smallest value
- take the smallest value in the pass and, if lowest j is different from i, swap places between i and lowest j
"""

def sort(list):
    
    last_index = len(list) - 1
    i = -1

    while i < last_index:
        i += 1

        lowest_val_j = i
        
        j = i - 1
        while j < last_index:
            j += 1

            if list[j] < list[lowest_val_j]: lowest_val_j = j
        
        if i == lowest_val_j: continue

        list[i], list[lowest_val_j] = list[lowest_val_j], list[i]

    return list

result = sort([3, 6, 1, 2, -100, 500, 9, 6, -1, -10])
print(result)