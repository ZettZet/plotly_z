from enum import Flag, auto


class Reim(Flag):
    RE = auto()
    IM = auto()
    BOTH = RE | IM
