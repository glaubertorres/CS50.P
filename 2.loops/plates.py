def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[:2].isalpha() or not (2 <= len(s) <= 6):
        return False

    invalid_inputs = ["!", ",", ".", "?", " "]
    for char in s:
        if char in invalid_inputs:
            return False

    i = 0
    while i < len(s):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

            else:
                break

        i += 1

    list_numbers = []
    for char in s:
        if char.isdigit():
            list_numbers.append(char)
            if list_numbers and list_numbers[0] == "0":
                return False


    else:
        return True


main()