def smallest_divisor(number):
    if number == 1:
        return 1
    stop_count = int(number ** 0.5)

    def recurs(div):
        if div > stop_count:
            return number
        if number % div == 0:
            return div
        return recurs(div + 2)

    if number % 2 == 0:
        return 2

    return recurs(3)
