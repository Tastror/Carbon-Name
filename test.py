import carbon_number


def test_all():
    for i in range(1, 1005):
        print(
            carbon_number.colored_num(i),
            carbon_number.carbon_name(i, colored=True) +
            carbon_number.green(carbon_number.suffix(0))
        )

def test_one():
    def input_num() -> int:
        while True:
            num = int(input("input the number of carbon: "))
            if num <= 0:
                print("carbon number error")
                continue
            break
        return num
    r = input_num()
    s = carbon_number.carbon_name(r, colored=True)
    print(carbon_number.colored_num(r))
    for i in range(0, 4):
        print(s + carbon_number.green(carbon_number.suffix(i)))


if __name__ == "__main__":

    # test_all()

    print(
        "the name of alkane with 11 carbons is",
        carbon_number.carbon_name(11) + carbon_number.suffix("alkane")
    )

    test_one()
