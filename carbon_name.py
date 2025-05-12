_name_list = [

    # name_list[x][0] uses for 1 ~ 9

    # name_list[x][1] use as the ones place's prefixes when the *tens* changed, order is <any>x, 1x, 2x, ...
    #   default for len(name_list[x][1]) > 0 is name_list[x][1][0]
    #   default for len(name_list[x][1]) == 0 is name_list[x][0] + connect_suffix

    # name_list[x][2] use as the tens, hundreds, thousands, etc. places' prefixes, order is x0, x00, x000, ...
    #   default for len(name_list[x][1]) > 0 is name_list[x][1][0] + name_list[0][2][num_of_right_zeros - 1]
    #   default for len(name_list[x][1]) == 0 is name_list[x][0] + connect_suffix + name_list[0][2][num_of_right_zeros - 1]

    # connect_suffix ("a") used when
    #   (1) len(name_list[x][1]) == 0, or
    #   (2) connecting tens, hundreds, thousands, etc.

    # prefix    prefix-change-before-tens       suffix
    # single    all     10      20              10      100     1000
    #                           two "icos" put here... (easy to add)
    ("",       ["",     "",     "i",    ],     ["cont", "ct",   "li"    ],),  # 0
    ("meth",   ["hen",  "un",   "heni", ],     ["dec",  "hect", "kili"  ],),  # 1
    ("eth",    ["do"    ],                     ["cos",  "dict", "dili"  ],),  # 2 (di- only use in 200, 2000, etc., not in xx2)
    ("prop",   ["tri"   ],                     ["triacont"],), # 3
    ("but",    ["tetra" ],                     [],),  # 4
    ("pent",   [], []),  # 5
    ("hex",    [], []),  # 6
    ("hept",   [], []),  # 7
    ("oct",    [], []),  # 8
    ("non",    [], []),  # 9
]

_connect_suffix = "a"

_suffix_list = [
    "yl",  # 基
    "ane",  # 烷
    "ene",  # 烯
    "yne",  # 炔
    "anol",  # 醇
    "anal",  # 醛
    "anone",  # 酮
    "anoic acid",  # 羧酸
    "anoate",  # 酯
]


def red(input: str) -> str:
    return "\033[31m" + input + "\033[0m"
def blue(input: str) -> str:
    return "\033[34m" + input + "\033[0m"
def purple(input: str) -> str:
    return "\033[35m" + input + "\033[0m"
def green(input: str) -> str:
    return "\033[32m" + input + "\033[0m"
def yellow(input: str) -> str:
    return "\033[33m" + input + "\033[0m"


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
            one_str = _name_list[one_num][1][0]
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
            ten_hundred_etc_str = _name_list[ten_hundred_etc_num][1][0] + _name_list[0][2][num_of_right_zeros - 1]
        else:
            ten_hundred_etc_str = _name_list[ten_hundred_etc_num][0] + _connect_suffix + _name_list[0][2][num_of_right_zeros - 1]
    else:
        ten_hundred_etc_str = _name_list[ten_hundred_etc_num][2][num_of_right_zeros - 1]
    if with_suffix_at_end:
        return ten_hundred_etc_str + _connect_suffix
    return ten_hundred_etc_str


# get the name of the given carbon number
def carbon_name(carbon_num: int, colored: bool = False) -> str:
    if type(carbon_num) is not int or carbon_num <= 0:
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
    if carbon_num <= 9999:
        thousand_num = carbon_num // 1000
        hundred_num = carbon_num % 1000 // 100
        ten_num = carbon_num % 100 // 10
        one_num = carbon_num % 10
        one_str = _get_one_str(one_num, ten_num)
        ten_str = _get_ten_hundred_etc_str(ten_num, 1, with_suffix_at_end=True)
        hundred_num = _get_ten_hundred_etc_str(hundred_num, 2, with_suffix_at_end=True)
        thousand_num = _get_ten_hundred_etc_str(thousand_num, 3)
        if colored:
            return blue(one_str) + red(ten_str) + purple(hundred_num) + yellow(thousand_num)
        return one_str + ten_str + hundred_num + thousand_num
    return str(carbon_num) + "-carbon-X"


def suffix(type_or_num, colored: bool = False) -> str:
    return_str = ""
    if type(type_or_num) is int:
        if type_or_num < 0 or type_or_num >= len(_suffix_list):
            return ""
        return_str = _suffix_list[type_or_num]
    elif type(type_or_num) is str:
        if type_or_num == "alkyl":  # 基
            return_str = _suffix_list[0]
        elif type_or_num == "alkane":  # 烷
            return_str = _suffix_list[1]
        elif type_or_num == "alkene":  # 烯
            return_str = _suffix_list[2]
        elif type_or_num == "alkyne":  # 炔
            return_str = _suffix_list[3]
        elif type_or_num == "alcohol":  # 醇
            return_str = _suffix_list[4]
        elif type_or_num == "aldehyde":  # 醛
            return_str = _suffix_list[5]
        elif type_or_num == "ketones":  # 酮
            return_str = _suffix_list[6]
        elif type_or_num == "acids":  # (羧)酸
            return_str = _suffix_list[7]
        elif type_or_num == "ester":  # 酯
            return_str = _suffix_list[8]
        else:
            return_str = ""
    else:
        return_str = ""
    if colored: return green(return_str)
    return return_str


def colored_num(num: int) -> str:
    if num <= 9:
        return blue(str(num % 10))
    if num <= 99:
        return red(str(num % 100 // 10)) + blue(str(num % 10))
    if num <= 999:
        return purple(str(num // 100)) + red(str(num % 100 // 10)) + blue(str(num % 10))
    if num <= 9999:
        return yellow(str(num // 1000)) + purple(str(num % 1000 // 100)) + red(str(num % 100 // 10)) + blue(str(num % 10))
    return str(num)
