string = input("Input:") 

vowels = ["a","e","i","o","u"]

for s in string:
    if s in vowels:
        string = string.replace(s, "")

print("Output:", string)

