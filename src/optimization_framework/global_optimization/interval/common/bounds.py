from flint import arb
from optimization_framework.core.problems import Problem1D

def derivative_bounds(problem: Problem1D, x_left: float, x_right: float):
    """
    Compute a rigorous enclosure of f'(x) over [x_left, x_right].

    The derivative function is supplied through problem.df and must support interval arithmetic using python-flint's arb objects

    :param problem: The optimization problem containing the derivative function
    :param x_left: The left endpoint of the interval
    :param x_right: The right endpoint of the interval
    :return: The lower and upper derivative bounds
    """

    midpoint = (x_left + x_right) / 2.0
    radius = (x_right - x_left) / 2.0

    X = arb(midpoint, radius)
    dX = problem.df(X)

    d_lower = dX.lower()
    d_upper = dX.upper()

    return d_lower, d_upper


def lower_bounds(x,
                 x_left, x_right,
                 f_left, f_right,
                 d_lower, d_upper):
    """
    Evaluate the left and right derivative-based lower bounds at a given point.

    :param x: point at which the bounds are evaluated
    :param x_left: left endpoint of the interval
    :param x_right: right endpoint of the interval
    :param f_left: objective value at the left endpoint
    :param f_right: objective value at the right endpoint
    :param d_lower: lower bound on the derivative
    :param d_upper: upper bound on the derivative
    :return: left and right lower-bound values
    """

    L_left = f_left + d_lower * (x - x_left)
    L_right = f_right + d_upper * (x - x_right)

    return L_left, L_right


