#python programming language
def generate_series(a):
    series = []
    for i in range(a):
        series.append(2 * i + 1)  # formula for odd number
    return series
a = int(input("Enter a number (a): "))
print("Output:", ", ".join(map(str,generate_series(a))))
