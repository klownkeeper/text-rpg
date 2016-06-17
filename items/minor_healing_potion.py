from items import Item


class MinorHealingPotion(Item):


    name = "minor_healing_potion"
    weight = 0.3
    gold = 50

    action_list = {
        "drink": {
            "damage": "1d8",
            "attack": 1,
        }
    }
        
    def action(self, world):
        """docstring for fname"""
        pass
