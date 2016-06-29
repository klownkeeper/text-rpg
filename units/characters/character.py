class Character(CommandMixin, Unit):
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

