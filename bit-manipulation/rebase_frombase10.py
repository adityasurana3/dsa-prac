def from_base10(number, base):
    if base < 2:
        raise ValueError("Base b must be >= 2")
    if number < 0:
        raise ValueError("Number b must be >= 0")
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        mod = number % base
        number //= base
        digits.insert(0, mod)
    return digits


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    return "".join([digit_map[d] for d in digits])


def rebase_from10(number, base):
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    sign = -1 if number < 0 else 1
    number *= sign
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = "-" + encoding
    return encoding


convert = rebase_from10(10, 2)
print(convert)
