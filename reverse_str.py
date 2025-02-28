def reverse_string(s):
    stack = list(s)  # Convert string to a list (stack)
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()  # Pop characters from the stack
    return reversed_s

print(reverse_string("hello"))  # Output: "olleh"

#OUTPUT
olleh
