import sys
from units import Unit
import readline
from decorators import enemy_exist

class CommandMixin(object):

    def wait_command(self, commands=[None], targets=[None]):
        while True:
            try:
                # readline.parse_and_bind("tab: complete")
                # def completer(text,state):
                #     results = commands + [None]
                #     return results[state]
                # readline.set_completer(completer)

                print(">>>>> player action:")
                line = input()
                print("<<<<<")
                return line
            except KeyboardInterrupt:
                print("<ctrl-c>: 'help' for more information")
                continue
            except EOFError:
                print("<ctrl-d>: Player quit")
                raise Exception("GameOver")

    def get_command(self, world):
        while True:
            command, *args = self.wait_command(
                commands=self.action_name_list,
                targets=self.enemy_list(world)).strip().split(" ")

            try:
                if command == "help":
                    print("help")
                    print("status")
                    print("action")
                    continue

                if command == "status":
                    print("unit status")
                    for idx, unit in zip(range(len(world.unit_list)), world.unit_list):
                        print("> %d (%s)" % (idx, unit.name), unit is self and "Me" or None)
                    continue

                if command == "action":
                    print("player actions:")
                    for a in self.action_name_list.keys():
                        print("> ", a)
                    continue

                if command in self.action_name_list:
                    return (command, *args)
            except Exception as e:
                print(e)
                pass

    def ask_next_level_class(self):
        return "Fighter"

    def ask_ability_bonus(self):
        """docstring for ask_ability_bonus"""
        return "unit_str"


class AbstractCharacter(CommandMixin, Unit):
    """
    Abstract characters
    Strength   Dexterity  Constitution  Intelligence  Wisdom   Charisma
    """

    char_goal = 100

    char_race = "human"
    char_gender = "male"
    char_alignment = "true_neutral"

    items = []

    @enemy_exist
    def action(self, world):
        command, *args = self.get_command(world)
        self.dispatch(command, world, *args)
