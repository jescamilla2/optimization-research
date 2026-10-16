from dataclasses import dataclass

@dataclass
class SearchInterval:
    """
    An active interval in the optimization search
    """

    x_left: float
    x_right: float
    f_left: float
    f_right: float
    d_lower: float
    d_upper: float
    characteristic: float
    x_char: float