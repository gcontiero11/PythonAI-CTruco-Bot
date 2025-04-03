class CardToPlay:
    def __init__(self, name):
        self.name = name

    @classmethod
    def of(cls, name):
        return cls(name)

    def __repr__(self):
        return f"CardToPlay({self.name})"