def main():
    t = convert(input('What time is it: '))

    if t < 8:
        print('breakfast time')

    elif t >= 12 and t <= 13:
        print('lunch time')

    elif t >= 18 and t <= 19:
        print('dinner time')


def convert(time):

    time = time.split(":")
    hours = float(time[0])
    minutes = float(time [1]) / 60
    clock = hours + minutes

    return clock

if __name__ == "__main__":
    main()