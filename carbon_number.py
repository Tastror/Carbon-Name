_name_list = [

    # name_list[x][0] use for 1 ~ 9
    
    # name_list[x][1] use as the ones place's prefixes, order is y0x, (y)1x, (y)2x, ...
    #   default for len(name_list[x][1]) > 0 is name_list[x][1][-1]
    #   default for len(name_list[x][1]) == 0 is name_list[x][0] + connect_suffix

    # name_list[x][2] use as the tens, hundreds, etc. places' prefixes, order is x0, x00, ...
    #   default for len(name_list[x][1]) > 0 is name_list[x][1][-1] + name_list[0][2][num_of_right_zeros - 1]
    #   default for len(name_list[x][1]) == 0 is name_list[x][0] + connect_suffix + name_list[0][2][num_of_right_zeros - 1]

    ("",        ["", "", "i", ""],              ["cont", "hect"],),     # 0
    ("meth",    ["hen", "un", "heni", "hen"],   ["dec", "hect"],),      # 1
    ("eth",     ["do"],                         ["cos"],),      # 2
    ("prop",    ["tri"],                        ["triacont"],), # 3
    ("but",     ["tetra"],                      [],),           # 4
    ("pent",    [], []),  # 5
    ("hex",     [], []),  # 6
    ("hept",    [], []),  # 7
    ("oct",     [], []),  # 8
    ("non",     [], []),  # 9
]

_connect_suffix = "a"

_suffix_list = [
    "ane",
    "ylene",
    "yne",
    "yl"
]


def red(input: str) -> str:
    return "\033[31m" + input + "\033[0m"
def blue(input: str) -> str:
    return "\033[34m" + input + "\033[0m"
def purple(input: str) -> str:
    return "\033[35m" + input + "\033[0m"
def green(input: str) -> str:
    return "\033[32m" + input + "\033[0m"


# 1 <= carbon number <= 9
# no suffix
def _get_only_one_str(one_num: int) -> str:
    assert(0 <= one_num <= 9)
    return _name_list[one_num][0]


# carbon number >= 10
# with suffix
def _get_one_str(one_num: int, ten_num: int) -> str:
    assert(0 <= one_num <= 9)
    assert(0 <= ten_num <= 9)
    if len(_name_list[one_num][1]) <= ten_num:
        if len(_name_list[one_num][1]) != 0:
            one_str = _name_list[one_num][1][-1]
        else:
            one_str = _name_list[one_num][0] + _connect_suffix
    else:
        one_str = _name_list[one_num][1][ten_num]
    return one_str


# carbon number >= 10
# with or no suffix (change with_suffix_at_end)
def _get_ten_hundred_etc_str(ten_hundred_etc_num: int, num_of_right_zeros: int, with_suffix_at_end: bool = False) -> str:
    assert(0 <= ten_hundred_etc_num <= 9)
    assert(num_of_right_zeros >= 1)
    if ten_hundred_etc_num == 0:
        return ""
    if len(_name_list[ten_hundred_etc_num][2]) < num_of_right_zeros:
        if len(_name_list[ten_hundred_etc_num][1]) != 0:
            ten_hundred_etc_str = _name_list[ten_hundred_etc_num][1][-1] + _name_list[0][2][num_of_right_zeros - 1]
        else:
            ten_hundred_etc_str = _name_list[ten_hundred_etc_num][0] + _connect_suffix + _name_list[0][2][num_of_right_zeros - 1]
    else:
        ten_hundred_etc_str = _name_list[ten_hundred_etc_num][2][num_of_right_zeros - 1]
    if with_suffix_at_end:
        return ten_hundred_etc_str + _connect_suffix
    return ten_hundred_etc_str


# get the name of the given carbon number
def carbon_name(carbon_num: int, colored: bool = False) -> str:
    if carbon_num <= 0:
        return ""
    if carbon_num <= 9:
        one_str = _get_only_one_str(carbon_num)
        if colored:
            return blue(one_str)
        return one_str
    if carbon_num <= 99:
        ten_num = carbon_num // 10
        one_num = carbon_num % 10
        one_str = _get_one_str(one_num, ten_num)
        ten_str = _get_ten_hundred_etc_str(ten_num, 1)
        if colored:
            return blue(one_str) + red(ten_str)
        return one_str + ten_str
    if carbon_num <= 999:
        hundred_num = carbon_num // 100
        ten_num = carbon_num % 100 // 10
        one_num = carbon_num % 10
        one_str = _get_one_str(one_num, ten_num)
        ten_str = _get_ten_hundred_etc_str(ten_num, 1, with_suffix_at_end=True)
        hundred_num = _get_ten_hundred_etc_str(hundred_num, 2)
        if colored:
            return blue(one_str) + red(ten_str) + purple(hundred_num)
        return one_str + ten_str + hundred_num
    return str(carbon_num) + "-carbon X"


def suffix(type_or_num) -> str:
    if type(type_or_num) is int:
        return _suffix_list[type_or_num]
    elif type(type_or_num) is str:
        if type_or_num == "alkane":
            return _suffix_list[0]
        elif type_or_num == "alkene":
            return _suffix_list[1]
        elif type_or_num == "alkyne":
            return _suffix_list[2]
        else:
            return _suffix_list[3]
    return ""


def colored_num(num: int) -> str:
    if num <= 9:
        return blue(str(num % 10))
    if num <= 99:
        return red(str(num % 100 // 10)) + blue(str(num % 10))
    if num <= 999:
        return purple(str(num // 100)) + red(str(num % 100 // 10)) + blue(str(num % 10))
    return str(num)
