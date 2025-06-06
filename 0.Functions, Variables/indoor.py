# WRITING IN ALL CAPS IS LIKE YELLING.

# Best to use your “indoor voice” sometimes, writing entirely in lowercase.

# In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

# https://cs50.harvard.edu/python/2022/psets/0/indoor/


# Case conversion utility using str.swapcase()
# Note: Non-alphabetic characters remain unaffected

x = input()  # Raw string input preserves original encoding
print(str.swapcase(x))