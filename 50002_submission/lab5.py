"""
a[R11] = 1234
b[R12] = 
R3: 
"""


def count_bulls_cows(a, b):
    """
    :param a: secret word
    :param b: test word
    :return:
    """
    print(f'inputs {hex(a)} {hex(b)}')

    cows = 0  # R1
    bulls = 0  # R2

    for k in range(3, -1, -1):
        # print('KKK', k)
        sa = a >> 4 * k
        ad = sa & 0xF
        a_counted = ad == 0xF
        if a_counted: continue

        is_cow = 0
        is_bull = 0
        last_cow_index = 4

        for i in range(3, -1, -1):
            sb = b >> 4 * i
            bd = sb & 0xF
            eq = ad == bd

            # a_counted = ad == 0xF
            # if a_counted: continue

            # last minute patch (a=2222, b=1234)
            # if the digit is a bull somewhere further
            # down the line we set it as NEVER a cow
            # here first
            sa2 = a >> 4 * i
            ad2 = sa2 & 0xF
            not_future_bull = ad2 != bd

            n_shifted = k == i
            shifted = 1 - n_shifted
            digit_is_bull = n_shifted * eq

            digit_is_cow = shifted * eq
            digit_is_cow *= not_future_bull
            is_bull |= digit_is_bull
            is_cow |= digit_is_cow

            print(
                f'i={i}', f'bd={hex(bd)}',
                f'd-bull={digit_is_bull} d-cow={digit_is_cow}'
            )

            if digit_is_cow:
                last_cow_index = i

            if not digit_is_bull:
                continue

            mask_b = 0xF << i * 4
            b |= mask_b
            last_cow_index = 4
            print(f'MASK4 {i*4}', hex(mask_b), hex(b))
            break

            # pos = (k, i)
            # print(pos, bd, ad, eq)
            # print(f'{pos} bulls = {bulls}, cows= {cows}')

        mask_b = 0xF << last_cow_index * 4
        b |= mask_b

        not_bull = 1 - is_bull
        is_cow = is_cow * not_bull
        cows += is_cow
        bulls += is_bull

        print(f'BULLS={bulls}', f'COWS={cows}')
        print(
            f'k={k}', f'ad={hex(ad)}', f'is_bull={is_bull}', 
            f'is_cow={is_cow}', hex(a), hex(b)
        )

        print('')
        # set digit to 0xF (invalid)
        # mask_b = 0xF << k * 4
        # b |= mask_b
        # mask_a = 0xF << i * 4
        # a |= mask_a

        # print(f'MASKED {hex(b)}')

    bull_shift = bulls << 4
    total = bull_shift + cows
    print(f'bulls = {bulls}, cows= {cows}\n')
    # print(hex(total))
    return total


assert count_bulls_cows(0x5700, 0x1003) == 0x11
assert count_bulls_cows(0x5593, 0x5975) == 0x12
assert count_bulls_cows(0x5593, 0x6057) == 0x01
assert count_bulls_cows(0x5593, 0x6075) == 0x01

print('compare aginst 2222')
assert count_bulls_cows(0x2222, 0x1234) == 0x10
print('')

print('comparing against 1234')
assert count_bulls_cows(0x1234, 0x2222) == 0x10
assert count_bulls_cows(0x1234, 0x1379) == 0x11
assert count_bulls_cows(0x1234, 0x4321) == 0x04
assert count_bulls_cows(0x1234, 0x1344) == 0x21
assert count_bulls_cows(0x1234, 0x1234) == 0x40
print('')

print('comparing against 2270')
assert count_bulls_cows(0x2270, 0x2208) == 0x21
assert count_bulls_cows(0x2270, 0x0227) == 0x13
assert count_bulls_cows(0x2270, 0x0000) == 0x10
assert count_bulls_cows(0x2270, 0x2207) == 0x22
