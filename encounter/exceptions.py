class NoEnemyException(BaseException):
    pass


class BattleFinishedException(BaseException):
    team_win = None

    def __init__(self, team_win, **kwargs):
        self.team_win = team_win
        return super(BattleFinishedException, self). __init__(**kwargs)


class SkillFailToCastException(BaseException):
    team_win = None

    def __init__(self, team_win, **kwargs):
        self.team_win = team_win
        return super(BattleFinishedException, self). __init__(**kwargs)
