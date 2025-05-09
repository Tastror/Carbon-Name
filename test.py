import carbon_name


def test_all():
    for i in range(1, 1005):
        print(
            carbon_name.colored_num(i),
            carbon_name.carbon_name(i, colored=True) +
            carbon_name.suffix(1, colored=True)
        )

def test_one():
    def input_num() -> int:
        while True:
            try:
                num = int(input("input the number of carbon: "))
            except ValueError:
                print("carbon number error")
                continue
            if num <= 0:
                print("carbon number error")
                continue
            break
        return num
    r = input_num()
    s = carbon_name.carbon_name(r, colored=True)
    print(carbon_name.colored_num(r))
    for i in range(0, 9):
        print(s + carbon_name.suffix(i, colored=True))


if __name__ == "__main__":

    # test_all()

    print(
        "the name of alkane with 11 carbons is ",
        carbon_name.carbon_name(11, colored=True) +
        carbon_name.suffix("alkane", colored=True),
    )

    while True:
        test_one()
