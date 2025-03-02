# Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

# Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.


# https://cs50.harvard.edu/python/2022/psets/0/faces/

def main():
    """Entry point: Processes input string and outputs emoji-converted result."""
    sentence = input()  # Raw text input preserves original formatting/whitespace
    sentence = convert(sentence)  # Core conversion logic encapsulated
    print(sentence)  # Direct output without formatting modifications

def convert(sentence: str) -> str:
    """Replaces text-based emoticons with Unicode emojis.
    
    Args:
        sentence: Input string containing potential emoticons
        
    Returns:
        Modified string with replacements:
        - ":)" → "🙂" 
        - ":(" → "🙁"
        
    Note:
        Performs sequential replacements in two passes. Case-sensitive.
        Does not handle mixed/overlapping patterns (e.g. "::))").
    """
    sentence = sentence.replace(":)", "🙂")  # First pass: positive emoticon
    sentence = sentence.replace(":(", "🙁")  # Second pass: negative emoticon
    return sentence

if __name__ == "__main__":
    main()  # Execute program when run directly