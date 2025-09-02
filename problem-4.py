def count_multiples(numbers):
    result = {}
    for i in range(1, 10):  # from 1 to 9
        count = sum(1 for num in numbers if num % i == 0)
        result[i] = count
    return result


# Example usage:
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(numbers))
