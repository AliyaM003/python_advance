def concatenate_lists(lst1, lst2):
    result = []
    min_length = min(len(lst1), len(lst2))  
    for i in range(min_length):
        result.append(lst1[i] + lst2[i])
    return result

print(concatenate_lists(['H', 'F', 'y'], ['i', 'i']))  # Output: ['Hi', 'Fi']


#OUTPUT
#['Hi', 'Fi']
