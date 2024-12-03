from collections import defaultdict

if __name__ == "__main__":
    left_dict = defaultdict(int)
    right_dict = defaultdict(int)
    result = 0
    
    with open("01_2/input.txt", 'r') as f:
        for line in f:
            first, second = map(int, line.split())
            left_dict[first] += 1
            right_dict[second] += 1

    for key, value in left_dict.items():
        if key in right_dict:
            result += value * key * right_dict[key]

    print(result)