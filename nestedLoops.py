print("Multiplication chart")

print("  ", end = '')

for j in range(1, 10):
    print("  ", j, end = '')

print()
print("---------------------------------------")

for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        print((f"{i * j: 4d}"), end = '')
    print()