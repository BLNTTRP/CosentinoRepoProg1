x = 0

while x < 30:
    x += 1

    if x == 15:
        print("The execution of the loop was broken when x was", x)
        break

    if x in [4, 6, 10]:
        print("The value", x, "of x was skipped")
        continue

    print("The value of the loop is:", x)
