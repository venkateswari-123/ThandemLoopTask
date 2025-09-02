#python programming language
def generate_series(a):
    # If 'a' is even, generate (a-1) odd numbers
    count = a if a % 2 != 0 else a - 1
    series = [2 * i + 1 for i in range(count)]
    return series
a = int(input("Enter a number (a): "))
print("Output:", ", ".join(map(str,generate_series(a))))
