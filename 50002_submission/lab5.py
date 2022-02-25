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
        print('KKK', k)
        sb = b >> 4 * k
        bd = sb & 0xF
        b_counted = bd == 0xF
        if b_counted: continue

        is_cow = 0
        is_bull = 0

        for i in range(4, 0, -1):
            sa = a >> 4 * i
            ad = sa & 0xF
            eq = ad == bd

            # a_counted = ad == 0xF
            # if a_counted: continue

            n_shifted = k == i
            shifted = 1 - n_shifted
            digit_is_bull = n_shifted * eq
            digit_is_cow = shifted * eq
            is_bull |= digit_is_bull
            is_cow |= digit_is_cow

            if not digit_is_bull: continue

            mask_a = 0xF << i * 4
            a |= mask_a

            # pos = (k, i)
            # print(pos, bd, ad, eq)
            # print(f'{pos} bulls = {bulls}, cows= {cows}')

        print(k, hex(bd), is_bull, is_cow)
        not_bull = 1 - is_bull
        is_cow = is_cow * not_bull
        cows += is_cow
        bulls += is_bull

        # set digit to 0xF (invalid)
        # mask_b = 0xF << k * 4
        # b |= mask_b
        # mask_a = 0xF << i * 4
        # a |= mask_a

        # print(f'MASKED {hex(b)}')

    bull_shift = bulls << 4
    total = bull_shift + cows
    print(f'bulls = {bulls}, cows= {cows}')
    # print(hex(total))
    return total


print('comparing against 1234')
count_bulls_cows(0x1234, 0x1379)
count_bulls_cows(0x1234, 0x4321)
count_bulls_cows(0x1234, 0x1344)
count_bulls_cows(0x1234, 0x1234)
print('')
print('comparing against 2270')
count_bulls_cows(0x2270, 0x2208)
count_bulls_cows(0x2270, 0x0227)
count_bulls_cows(0x2270, 0x0000)
count_bulls_cows(0x2270, 0x2207)
