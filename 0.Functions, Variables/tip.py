# In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

# Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

# dollars_to_float, which should accept a str as input (formatted as $**.**, wherein each * is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
# percent_to_float, which should accept a str as input (formatted as **%, wherein each * is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
# Assume that the user will input values in the expected formats.


# https://cs50.harvard.edu/python/2022/psets/0/tip/


def main():
    """Main workflow: Collects user input, calculates tip, and displays result."""
    dollars = dollars_to_float(input("How much was the meal? "))  # Expects currency format ($##.##)
    percent = percent_to_float(input("What percentage would you like to tip? "))  # Expects percentage format (##%)
    tip = dollars * percent  # Mathematical operation requires clean numerical values
    print(f"Leave ${tip:.2f}")  # Formatting enforces proper monetary display

def dollars_to_float(d: str) -> float:
    """Converts currency string to float.
    
    Args:
        d: Input string with leading dollar sign (e.g., '$50.00')
        
    Returns:
        Float representation of monetary amount
        
    Note:
        - Only strips leading '$' characters
        - No validation for numeric characters after $
        - Potential ValueError if non-numeric remainder
    """
    d = d.lstrip('$')  # Remove ALL leading dollar signs (e.g., '$$50' → '50')
    return float(d)  # Will crash on values with commas (e.g., '$1,000')

def percent_to_float(p: str) -> float:
    """Converts percentage string to decimal equivalent.
    
    Args:
        p: Input string with trailing % (e.g., '15%')
        
    Returns:
        Decimal equivalent (e.g., 0.15 for '15%')
        
    Note:
        - Only strips trailing '%' characters
        - No validation for numeric characters before %
        - Handles whole numbers only (no decimal percentages)
    """
    p = p.rstrip('%')  # Remove ALL trailing % signs (e.g., '20%%' → '20')
    return float(p) / 100  # Convert percentage to decimal (15 → 0.15)

main()