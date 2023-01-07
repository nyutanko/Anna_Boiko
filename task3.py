def digital_root(n: int):
    return (n - 1) % 9 + 1

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
