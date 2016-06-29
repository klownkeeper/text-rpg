import random


def dice(dice_str):
    n, d = map(int, dice_str.split('d'))
    res = 0
    for i in range(n):
        res += random.choice(range(1, d+1))
    return res

def saving_throw_success(dc, bonus):
    return dc < dice("1d20") + bonus

def target_attack_print(**kwargs):
    fmt = " ".join([
            "  \033[94m{player_name}\033[0m try to attack",
            "to \033[91m{target_name}\033[0m,"])
    print(fmt.format(**kwargs))

def target_attack_failed_print(**kwargs):
    fmt = " ".join([
            "  \033[94m{player_name}\033[0m try to attack",
            "to \033[91m{target_name}\033[0m,",
            "but \033[91mFailed!\033[0m"])
    print(fmt.format(**kwargs))

def target_hit_print(**kwargs):
    fmt = " ".join([
            "  \033[94m{player_name}\033[0m attack using \033[94m\033[4m{action_name}\033[0m",
            "to \033[91m{target_name}\033[0m,",
            "deal \033[94m{damage}\033[0m damage (HP:\033[91m{target_hp}\033[0m).",
            "{message}"])
    print(fmt.format(**kwargs))

def cast_spell_print(**kwargs):
    fmt = " ".join([
            "  \033[94m{name}\033[0m is casting \033[94m\033[4m{spell_name}\033[0m"])
    print(fmt.format(**kwargs))

def cast_spell_success_print(**kwargs):
    fmt = " ".join([
            "  casting \033[94m\033[4m{spell_name}\033[0m successfully",
            "on \033[93m{target_name}\033[0m.",
            "{message}"])
    print(fmt.format(**kwargs))

def turn_start_print(**kwargs):
    fmt = " ".join([
            "\033[94m\033[4m{name}\033[0m's turn is started: "])
    print(fmt.format(**kwargs))

def turn_end_print(**kwargs):
    fmt = " ".join([
            "\033[94m\033[4m{name}\033[0m's turn is finished: "])
    print(fmt.format(**kwargs))
