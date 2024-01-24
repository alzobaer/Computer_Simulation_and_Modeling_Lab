def linear_congruential_method(seed, a, c, mod):
    x = seed
    random_numbers = []

    itr = 20
    while itr:
        random_numbers.append(x)
        x = (a * x + c) % mod
        if x == random_numbers[0]:
            break
        itr = itr - 1
    return random_numbers


def main():
    seed, a, c, mod = 0, 1, 3, 10   
    random_numbers = linear_congruential_method(seed, a, c, mod)
    print(random_numbers)


if __name__ == "__main__":
    main()