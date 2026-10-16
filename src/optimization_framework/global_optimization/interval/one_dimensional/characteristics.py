from optimization_framework.global_optimization.interval.common.bounds import lower_bounds

def interval_characteristic(x_left, x_right, f_left, f_right, d_lower, d_upper):
    """
    Compute the characteristic R(X) and the point where it is attained.
    :param x_left: left endpoint of the interval
    :param x_right: right endpoint of the interval
    :param f_left: objective value at the left endpoint
    :param f_right: objective value at the right endpoint
    :param d_lower: lower bound on the derivative
    :param d_upper: upper bound on the derivative
    :return: tuple containing the characteristic and the point where it is attained
    """

    # Function is nondecreasing over the entire interval
    if d_lower >= 0:
        return f_left, x_left

    # Function is nonincreasing over the entire interval
    if d_upper <= 0:
        return f_right, x_right

    # Find the intersection by setting the two lower bounds equal and solving for x:
    # f_left + d_lower * (x - x_left) = f_right + d_upper * (x - x_right)
    # x = (f_right - f_left + d_lower * x_left - d_upper * x_right) / (d_lower - d_upper)
    x_char = (f_right - f_left + d_lower * x_left - d_upper * x_right) / (d_lower - d_upper)

    # Ensure the intersection point lies within the interval
    if x_char < x_left:
        x_char = x_left
    elif x_char > x_right:
        x_char = x_right

    # Evaluate both lower-bound lines at the selected point using the helper function lower_bounds()
    L_left, L_right = lower_bounds(x_char,
                                   x_left, x_right,
                                   f_left, f_right,
                                   d_lower, d_upper)

    # The tighter lower bound determines the characteristic
    characteristic = max(L_left, L_right)

    return characteristic, x_char