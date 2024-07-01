numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
def is_odd(number):
    return number % 2 != 0
def square(number):
    return number ** 2
odd_numbers = filter(is_odd, numbers)
odd_squares = map(square, odd_numbers)
result = list(odd_squares)
print(result)
