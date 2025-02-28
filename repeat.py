def find_repeated(numbers):
    seen = set()
    repeated = set()
    
    for num in numbers:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    
    return list(repeated)  
numbers = [2, 3, 5, 57, 56,7,57]
repeated_numbers = find_repeated(numbers)

if repeated_numbers:  
    print("Repeated numbers are:", repeated_numbers)
else:
    print("Repeated numbers not found.")

#OUTPUT
Repeated numbers are: [57]
