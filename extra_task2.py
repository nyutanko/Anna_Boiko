def int32_to_ip(int32):
    bin_str = f'{int32:b}'.rjust(32, '0')
    return '.'.join([str(int(bin_str[idx:idx + 8], 2)) for idx in range(0, len(bin_str), 8)])

print(int32_to_ip(2149583361))
print(int32_to_ip(32))
print(int32_to_ip(0))
