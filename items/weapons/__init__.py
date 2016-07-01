from items.damage_types import *
from items.weapon_types import *


UNARMED_STRIKE_SMALL = {
    "name": "unarmed_strike_small",
    "description": "Unarmed strike, Small size.",
    'weapon_types': [SIMPLE, UNARMED, LIGHT, MELEE],
    'damage': '1d2',
    'damage_type': DAMAGE_BLUDGEONING,
    'critical_times': 2,
    'critical_dice': [20],
    'cost': '0',
    'weight': 0,
    'hp': None,
    'effect': None,
}

UNARMED_STRIKE_MEDIUM = {
    "name": "unarmed_strike_medium",
    "description": "Unarmed strike, Midium size.",
    'weapon_types': [SIMPLE, UNARMED, LIGHT, MELEE],
    'damage': '1d3',
    'damage_type': DAMAGE_BLUDGEONING,
    'critical_times': 2,
    'critical_dice': [20],
    'cost': '0',
    'weight': 0,
    'hp': None,
    'effect': None,
}

CLUB_SMALL = {
    "name": "club_small",
    "description": "A club, short. Small size.",
    'weapon_types': [SIMPLE, ONE_HANDED, THROWN, MELEE],
    'damage': '1d4',
    'damage_type': DAMAGE_BLUDGEONING,
    'critical_times': 2,
    'critical_dice': [20],
    'cost': '0',
    'weight': 1.0,
    'hp': 2,
    'effect': None,
}

SHORT_SWORD_SMALL = {
    "name": "short_sword_small",
    "description": "A sword, short. Small size.",
    'weapon_types': [MARTIAL,LIGHT, MELEE],
    'damage': '1d4',
    'damage_type': DAMAGE_PIERCING,
    'critical_times': 2,
    'critical_dice': [19, 20],
    'cost': '10',
    'weight': 1.0,
    'hp': 1,
    'effect': None,
}

SHORT_SWORD_MEDIUM = {
    "name": "short_sword_medium",
    "description": "A sword, short. Medium size.",
    'weapon_types': [MARTIAL,LIGHT, MELEE],
    'damage': '1d6',
    'damage_type': DAMAGE_PIERCING,
    'critical_times': 2,
    'critical_dice': [19, 20],
    'cost': '10',
    'weight': 2.0,
    'hp': 2,
    'effect': None,
}
