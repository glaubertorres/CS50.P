c = input('Expression: ').split(' ')

x,y,z = float(c[0]), c[1], float(c[2])

if y == '+':
    result = x + z
    print(result)

elif y == '-':
    result = x - z
    print(result)

elif y == '*':
    result = x * z
    print(result)

else:
    result = x / z
    print(result)

