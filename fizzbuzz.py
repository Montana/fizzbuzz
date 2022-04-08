def fizzbuzz(n):
    fizz = n % 3 == 0
    buzz = n % 5 == 0
    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return str(n)


print(list(map(fizzbuzz, range(1, 100 + 1))))


fizzbuzz = lambda n: [
    ["FizzBuzz", "Fizz", "Buzz", str(n)][
        (0 if (n % 3) == 0 else 1) + (0 if (n % 5) == 0 else 2)
    ]
    for n in range(1, n + 1)
]
print(fizzbuzz(100))


def fizzbuzz():
    sieve = [0] * 15
    for x in range(0, 15, 3):
        sieve[x] += 1
    for x in range(0, 15, 5):
        sieve[x] += 2

    def fizzbuzz(n):
        return ["{n}", "Fizz", "Buzz", "FizzBuzz"][sieve[n % 15]].format(**locals())

    return lambda n: list(map(fizzbuzz, range(1, n + 1)))


fizzbuzz = fizzbuzz()
print(fizzbuzz(100))


def fizzbuzz():
    fill = lambda s, k, v: [x + v if i % k == 0 else x for i, x in enumerate(s)]
    s = fill(fill([0] * 15, 3, 1), 5, 2)

    def fizzbuzz(n):
        return ["{n}", "Fizz", "Buzz", "FizzBuzz"][s[n % 15]].format(**locals())

    return lambda n: list(map(fizzbuzz, range(1, n + 1)))


fizzbuzz = fizzbuzz()
print(fizzbuzz(100))


def fizzbuzz():
    fill = lambda s, k, v: [x + v if i % k == 0 else x for i, x in enumerate(s)]
    s = fill(fill([0] * 15, 3, 1), 5, 2)
    return lambda n: [
        [str(n), "Fizz", "Buzz", "FizzBuzz"][s[n % 15]] for n in range(1, n + 1)
    ]

    def fizzbuzz(n):
        return ["{n}", "Fizz", "Buzz", "FizzBuzz"][s[n % 15]].format(**locals())

    return lambda n: list(map(fizzbuzz, range(1, n + 1)))


fizzbuzz = fizzbuzz()
print(fizzbuzz(100))


def fizzbuzz():
    def branch(n):
        l = [(n - 1) >> 1] + [0] * (n - 1)
        return lambda p: p[1] + l[p[0] % n]

    fill = lambda xs, n: list(map(branch(n), enumerate(xs)))
    xs = fill(fill([0] * 15, 3), 5)
    return lambda n: [
        ["{n}", "Fizz", "Buzz", "FizzBuzz"][xs[n % 15]].format(**locals())
        for n in range(1, n + 1)
    ]


fizzbuzz = fizzbuzz()
print(fizzbuzz(100))
