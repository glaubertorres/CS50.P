def main():
    while True:
        frac = input("Fraction: ")

        try:
            # split input
            n, d = frac.split("/")

            # str to int
            x = int(n)
            y = int(d)

            # calculate the fraction
            result = x / y

            # break the loop it result <= 1
            if result <= 1:
                break

        except(ValueError, ZeroDivisionError):
            pass

    # multiply fraction
    tank = result * 100

    # round to nearest int
    tank = round(tank)

    # output
    if tank <= 1:
        print("E")

    elif tank >=99:
        print("F")

    else:
        print("%i%%" %tank)

main()



