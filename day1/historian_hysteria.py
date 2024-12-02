import bisect
from collections import Counter

list_a = []
list_b = []

def populate_list(filename):
    file = open(filename, 'r')
    for line in file:
        a, b = line.split()
        # Sort the list as we insert
        bisect.insort(list_a, a)
        bisect.insort(list_b, b)


def get_distance():
    distance = 0
    for i in range(len(list_a)):
        distance += abs(int(list_a[i]) - int(list_b[i]))
    return distance

def get_similarity():
    similarity = 0
    # Get the count of each number in list_b
    list_b_counts = Counter(list_b)
    for i in range(len(list_a)):
        number = list_a[i]
        if number in list_b_counts:
            similarity += list_b_counts[number] * int(number)
    return similarity

def main():
    populate_list('input.txt')
    # print(get_distance())
    print(get_similarity())

if __name__ == "__main__":
    main()