from encounter.exceptions import NoEnemyException


def enemy_exist(func):
    """
    make sure enemy_exist, or raise Success
    """

    def func_wrapper(obj, world, *args, **kwargs):
        """docstring for func_wrapper"""
        enemy_list = obj.enemy_list(world)
        if not enemy_list:
            raise NoEnemyException
        return func(obj, world, *args, **kwargs)

    return func_wrapper
