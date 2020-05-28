from nari.util.pair import IdNamePair

class Ability(IdNamePair):
    def __repr__(self) -> str:
        return f'<Ability ({self.name})>'