import random


def dice(dice_str):
    n, d = map(int, dice_str.split('d'))
    res = 0
    for i in range(n):
        res += random.choice(range(1, d+1))
    return res


def saving_throw_success(dc, bonus):
    return dc < dice("1d20") + bonus
