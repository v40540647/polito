def main():
    """Main entry point"""
    number = int(input("Number: "))
    base = int(input("Base: "))
    value = convert10(number, base)
    print(f"{number}|{base} = {value}|10")


def convert10(number, base):
    value = 0
    for n, d in enumerate(reversed(str(number))):
        value = value + int(d) * base ** n
    return value


if __name__ == '__main__':
    main()