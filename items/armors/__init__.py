from items.armor_types import *
from items.weapon_types import *
from items.damage_types import *


PADDED_SMALL = {
    "name": "padded_small",
    "description": "",
    'armor_type': LIGHT_ARMOR,
    'armor_bonus': 1,
    'armor_check_penalty': 0,
    'max_dex_bonus': 8,
    'cost': 5,
    'weight': 5.0,
    'hp': 2,
    'effect': None,
    'arcane_spell_failure_dice': [1],
}

PADDED_MEDIUM = {
    "name": "padded_medium",
    "description": "",
    'armor_type': LIGHT_ARMOR,
    'armor_bonus': 1,
    'armor_check_penalty': 0,
    'max_dex_bonus': 8,
    'cost': 5,
    'weight': 10.0,
    'hp': 5,
    'effect': None,
    'arcane_spell_failure_dice': [1],
}

HIDE_SMALL = {
    "name": "hide_small",
    "description": "",
    'armor_type': MEDIUM_ARMOR,
    'armor_bonus': 3,
    'armor_check_penalty': -3,
    'max_dex_bonus': 4,
    'cost': 15,
    'weight': 12.5,
    'hp': 7,
    'effect': None,
    'arcane_spell_failure_dice': [1, 2, 3, 4],
}

HIDE_MEDIUM = {
    "name": "hide_medium",
    "description": "",
    'armor_type': MEDIUM_ARMOR,
    'armor_bonus': 3,
    'armor_check_penalty': -3,
    'max_dex_bonus': 4,
    'cost': 15,
    'weight': 25.0,
    'hp': 15,
    'effect': None,
    'arcane_spell_failure_dice': [1, 2, 3, 4],
}

SPLINT_MAIL_SMALL = {
    "name": "splint_mail_medium",
    "description": "",
    'armor_type': HEAVY_ARMOR,
    'armor_bonus': 6,
    'armor_check_penalty': -7,
    'max_dex_bonus': 0,
    'cost': 200,
    'weight': 22.5,
    'hp': 15,
    'effect': None,
    'arcane_spell_failure_dice': [1, 2, 3, 4, 5, 6, 7, 8],
}

SPLINT_MAIL_MEDIUM = {
    "name": "splint_mail_medium",
    "description": "",
    'armor_type': HEAVY_ARMOR,
    'armor_bonus': 6,
    'armor_check_penalty': -7,
    'max_dex_bonus': 0,
    'cost': 200,
    'weight': 45.0,
    'hp': 30,
    'effect': None,
    'arcane_spell_failure_dice': [1, 2, 3, 4, 5, 6, 7, 8],
}

LIGHT_WOOD_SHIELD_SMALL = {
    "name": "light_shield_small",
    "description": "",
    'weapon_types': [MARTIAL, LIGHT, MELEE],
    'damage': '1d2',
    'damage_type': DAMAGE_BLUDGEONING,
    'armor_type': SHIELD,
    'armor_bonus': 1,
    'armor_check_penalty': -1,
    'max_dex_bonus': None,
    'cost': 200,
    'weight': 2.5,
    'hp': 3,
    'effect': None,
    'arcane_spell_failure_dice': [1],
}

LIGHT_WOOD_SHIELD_MEDIUM = {
    "name": "light_shield_medium",
    "description": "",
    'weapon_types': [MARTIAL, LIGHT, MELEE],
    'damage': '1d3',
    'damage_type': DAMAGE_BLUDGEONING,
    'armor_type': SHIELD,
    'armor_bonus': 1,
    'armor_check_penalty': -1,
    'max_dex_bonus': None,
    'cost': 200,
    'weight': 5.0,
    'hp': 3,
    'effect': None,
    'arcane_spell_failure_dice': [1],
}
