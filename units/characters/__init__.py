import sys
from units import Unit

class CommandMixin(object):

    def wait_stdin(self):
        while True:
            try:
                print("input command:")
                line = sys.stdin.readline()
                print("get command:", line)
                return line
            except KeyboardInterrupt:
                print("<ctrl-c>: 'help' for more information")
                pass

    def get_command(self, world):
        while True:
            raw_command = self.wait_stdin().strip()
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


class Character(CommandMixin, Unit):
    """
    Abstract characters
    Strength   Dexterity  Constitution  Intelligence  Wisdom   Charisma
    """
    char_str = 10
    char_dex = 10
    char_con = 10
    char_int = 10
    char_wis = 10
    char_chr = 10

    char_level = 1
    char_goal = 100

    char_race = "human"
    char_gender = "male"
    char_alignment = "true_neutral"

    action_list = {}
    items = []

    def action(self, world):
        # command, target = self.get_command(world)
        raise NotImplementedError
