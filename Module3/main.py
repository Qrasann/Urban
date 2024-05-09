def test(*args, **args2):
    print("Позиционные аргументы:")
    for arg in args:
        print(arg)

    print("\nКлючевые аргументы:")
    for key, value in args2.items():
        print(f"{key}: {value}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


test('solo', 322, string = "I love minecraft", num = 24)
print(factorial(4))
