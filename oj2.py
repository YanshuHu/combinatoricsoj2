def main():
    variable1 = input()
    variable2 = input()
    a = variable1.split()
    b = variable2.split()
    first_line = []
    second_line = []
    for i in a:
        first_line.append(int(i))
    for i in b:
        second_line.append(int(i))
    code(first_line[0], second_line)


def code(target, number):
    ways = [1]+[0]*target
    for value in number:
        for i in range(value, target+1):
            ways[i] += ways[i-value]
    print(ways[target])


if __name__ == '__main__':
    main()
