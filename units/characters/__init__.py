import sys
from units import Unit
import readline
from decorators import enemy_exist

class CommandMixin(object):

    def wait_command(self, commands=[None], targets=[None]):
        while True:
            try:
                readline.parse_and_bind("tab: complete")
                def completer(text,state):
                    results = commands + [None]
                    return results[state]
                readline.set_completer(completer)

                line = input("input command:")
                return line
            except KeyboardInterrupt:
                print("<ctrl-c>: 'help' for more information")
                continue
            except EOFError:
                print("<ctrl-d>: Player quit")
                raise Exception("GameOver")

    def get_command(self, world):
        while True:
            raw_command = self.wait_command(
                commands=list(self.action_list.keys()),
                targets=self.enemy_list(world)).strip()

            try:
                if raw_command == "help":
                    print("help: this")
                    print("status: all unit status")
                    print("commands: my commands")
                    continue

                if raw_command == "status":
                    print("units")
                    for idx, unit in zip(range(len(world.unit_list)), world.unit_list):
                        print("> %d (%s)" % (idx, unit.name), unit is self and "Me" or None)
                    continue

                if raw_command == "commands":
                    print("actions")
                    for a in self.action_list.keys():
                        print("> ", a)
                    continue

                command, target_id = raw_command.split(' ')

                if command in self.action_list:
                    return (command, int(target_id))
            except Exception as e:
                print(e)
                pass

    def ask_next_level_class(self):
        return "Fighter"


class AbstractCharacter(CommandMixin, Unit):
    """
    Abstract characters
    Strength   Dexterity  Constitution  Intelligence  Wisdom   Charisma
    """

    char_level = 1
    char_goal = 100

    char_race = "human"
    char_gender = "male"
    char_alignment = "true_neutral"

    action_list = {}
    items = []

    @enemy_exist
    def action(self, world):
        command, *args = self.get_command(world)
        self.dispatch(command, world, *args)
