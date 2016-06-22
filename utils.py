import random


def dice(dice_str):
    n, d = map(int, dice_str.split('d'))
    res = 0
    for i in range(n):
        res += random.choice(range(1, d+1))
    return res

def saving_throw_success(dc, bonus):
    return dc < dice("1d20") + bonus

def target_hit_print(**kwargs):
    fmt = " ".join([
            "  \033[94m{player_name}\033[0m do \033[94m\033[4m{action_name}\033[0m",
            "to \033[91m{target_name}\033[0m,",
            "deal \033[94m{damage}\033[0m damage (HP:\033[91m{target_hp}\033[0m).",
            "{message}"])
    print(fmt.format(**kwargs))

def target_heal_print(**kwargs):
    fmt = " ".join([
            "  \033[94m{name}\033[0m do \033[94m\033[4m{action_name}\033[0m",
            "to \033[93m{target_name}\033[0m,",
            "head \033[94m{damage}\033[0m damage (HP:\033[91m{target_hp}\033[0m).",
            "{message}"])
    print(fmt.format(**kwargs))
