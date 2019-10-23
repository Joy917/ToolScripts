
# dividend——被除数，divisor——除数，remainder——余数
def ex_gcd(dividend, divisor):
    if 0 == divisor:
        # 易证明：当除数等于0时，可得 X = 1， Y = 0。假设最大公因数为被除数。
        # 注意：数学上，0和自然数没有最大公因数，此处是为了方便理解。
        return 1, 0, dividend

    # 得到 X2 和 Y2 的值，并且将求最大公因数的步骤混入其中了
    x2, y2, remainder = ex_gcd(divisor, dividend % divisor)

    # 得到 X1 和 Y1 的值
    temp = x2
    x1 = y2
    y1 = temp - int((dividend // divisor) * y2)

    return x1, y1, remainder


if __name__ == "__main__":
    print(ex_gcd(101, 4620))
