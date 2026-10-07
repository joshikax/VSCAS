def calculate_total(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total = total + number

    return total


numbers = [10, 20, 30]
result = calculate_total(numbers)

print(result)