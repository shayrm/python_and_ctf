# Building an Exponent function
# the short method is A ** B but we could do the same with for loop

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))     # result = 8
print(raise_to_power(2, 16))    # result = 65536