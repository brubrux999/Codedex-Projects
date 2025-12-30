print("===============")
print("Area calculator")
print("===============")

print("1) Triangle\n2) Rectangle\n3) Square\n4) Circule\n5) Quit")

calculate = True

while calculate == True:
    shape = int(input("Which shape (1-5)?: "))

    # Triangle area
    if shape == 1:
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = base * height / 2
        print(f"The area is {area}")

    # Rectangle area
    elif shape == 2:
        width = float(input("Width: "))
        length = float(input("Length: "))
        area = width * length
        print(f"The area is {area}")

    # Square area
    elif shape == 3:
        side = float(input("Side: "))
        area = side**2
        print(f"The area is {area}")

    # Circule area
    elif shape == 4:
        radius = float(input("Radius: "))
        area = (radius**2) * 3.14
        print(f"The area is {area}")

    # Quit
    elif shape == 5:
        print("See you later!")
        break

    else:
        print("Invalid output")

    # Ask for another shape
    continue_ = input("Another one (y/n)? ")
    if continue_ == "n":
        print("Thank you for using this calculator!")
        calculate = False