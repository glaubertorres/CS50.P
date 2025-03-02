# Even if you haven’t studied physics (recently or ever!), you might have heard that E=mc^2, wherein E represents energy (measured in Joules), m represents mass (measured in kilograms), and c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.


# https://cs50.harvard.edu/python/2022/psets/0/einstein/


m = int(input())  # Requires integer input - no validation for negative/zero values
c = 300000000     # Approximate speed of light (exact SI value: 299792458 m/s)
e = m * pow(c, 2) # Using pow() for explicit squaring operation

print(e)          # Raw output with potential integer overflow for large masses
