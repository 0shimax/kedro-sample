def _is_true(x):
    return x == "t"


def _parse_percentage(x):
    x = x.str.replace("%", "")
    x = x.astype(float) / 100
    return x


def _parse_money(x):
    x = x.str.replace("$", "").str.replace(",", "")
    x = x.astype(float)
    return x
