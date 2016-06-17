class Item(object):

    name = None
    weight = 0.0
    gold = 0

    action_list = {}

    def action(self, action, **kwargs):
        raise NotImplementedError
