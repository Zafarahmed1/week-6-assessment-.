def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


numbers = [10, 501, 22, 37, 100, 999, 87, 351]


count = sum(1 for num in numbers if is_happy_number(num))

print("Number of happy numbers in the list:", count)