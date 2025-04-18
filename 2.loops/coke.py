price = 50
total = 0

while True:
    print("Amount Due: ", price - total)
    if total < price:
        coin = int(input("Insert Coin: "))
        while True:
            if coin == 30:
                coin = 0

            else:
                break

        total += coin

        continue

    else:
        print("change owed:", total - price)
        break