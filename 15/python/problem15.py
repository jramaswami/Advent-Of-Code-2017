"""
Advent of Code 2017 :: Day 15
Dueling Generators
"""
import tqdm

FACTOR_A = 16807
START_A = 679
FACTOR_B = 48271
START_B = 771
GENERATOR_MODULUS = 2147483647
MASK = 0b1111111111111111


def generator(factor, starting_val, iteration_limit=0):
    """Generates sequence of values."""
    prev_val = starting_val
    iter_count = 1
    while True:
        next_val = (prev_val * factor) % GENERATOR_MODULUS
        yield next_val
        if iteration_limit and iter_count >= iteration_limit:
            return
        iter_count += 1
        prev_val = next_val


def solve_a(start_a, start_b):
    """Solution to first part of puzzle."""
    limit = 40000000
    gen_a = generator(FACTOR_A, start_a, limit)
    gen_b = generator(FACTOR_B, start_b, limit)
    return sum((MASK & a) == (MASK & b) for a, b in zip(gen_a, gen_b))


def solve_a0(start_a, start_b):
    """Solution to first part of puzzle with progress bar."""
    limit = 40000000
    gen_a = generator(FACTOR_A, start_a)
    gen_b = generator(FACTOR_B, start_b)
    result = 0
    for _ in tqdm.tqdm(range(limit)):
        a = next(gen_a)
        b = next(gen_b)
        if (MASK & a) == (MASK & b):
            result += 1
    return result


def solve_b0(start_a, start_b):
    """Solution to second part of puzzle with progress bar."""
    limit = 5000000
    gen_a = filter(lambda a: a % 4 == 0, generator(FACTOR_A, start_a))
    gen_b = filter(lambda b: b % 8 == 0, generator(FACTOR_B, start_b))
    result = 0
    for _ in tqdm.tqdm(range(limit)):
        a = next(gen_a)
        b = next(gen_b)
        if (MASK & a) == (MASK & b):
            result += 1
    return result


def main():
    """Main Program."""
    result_a = solve_a0(START_A, START_B)
    print('The solution to part A is', result_a)
    result_b = solve_b0(START_A, START_B)
    print('The solution to part B is', result_b)


if __name__ == '__main__':
    main()