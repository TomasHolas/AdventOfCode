if __name__ == "__main__":
    first_list = []
    second_list = []
    result = 0

    with open("01_1/input.txt", 'r') as f:
        for line in f:
            first, second = line.split()
            first_list.append(int(first))
            second_list.append(int(second))

    first_list.sort()
    second_list.sort()
    
    for i, j in zip(first_list, second_list):
        result += abs(i-j)

    print(result)