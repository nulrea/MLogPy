from . import subFunction


op_add = subFunction('op', 'add', 'result', 'op1', 'op2', max_args=3)
op_sub = subFunction('op', 'sub', 'result', 'op1', 'op2', max_args=3)
op_mul = subFunction('op', 'mul', 'result', 'op1', 'op2', max_args=3)
op_div = subFunction('op', 'div', 'result', 'op1', 'op2', max_args=3)
"""
Division.

Returns `null` on divide-by-zero.
"""
op_idiv = subFunction('op', 'idiv', 'result', 'op1', 'op2', max_args=3)
"""
Integer division.
"""
op_mod = subFunction('op', 'mod', 'result', 'op1', 'op2', max_args=3)
"""
Modulo.
"""
op_pow = subFunction('op', 'pow', 'result', 'op1', 'op2', max_args=3)
op_eq = subFunction('op', 'equal', 'result', 'op1', 'op2', max_args=3)
"""
Equal. Coerces types.
Non-null objects compared with numbers become 1, otherwise 0.
"""
op_neq = subFunction('op', 'notEqual', 'result', 'op1', 'op2', max_args=3)
"""
Not equal. Coerces types.
"""
op_land = subFunction('op', 'land', 'result', 'op1', 'op2', max_args=3)
"""
Logical AND.
"""
op_lt = subFunction('op', 'lessThan', 'result', 'op1', 'op2', max_args=3)
op_le = subFunction('op', 'lessThanEq', 'result', 'op1', 'op2', max_args=3)
op_gt = subFunction('op', 'greaterThan', 'result', 'op1', 'op2', max_args=3)
op_ge = subFunction('op', 'greaterThanEq', 'result', 'op1', 'op2', max_args=3)
op_seq = subFunction('op', 'strictEqual', 'result', 'op1', 'op2', max_args=3)
"""
Strict equal. Does not coerce types.

Can be used to check for `null`.
"""
op_lshift = subFunction('op', 'shl', 'result', 'op1', 'op2', max_args=3)
"""
Bit-shift left.
"""
op_rshift = subFunction('op', 'shr', 'result', 'op1', 'op2', max_args=3)
"""
Bit-shift right.
"""
op_or = subFunction('op', 'or', 'result', 'op1', 'op2', max_args=3)
"""
Bitwise OR.
"""
op_and = subFunction('op', 'and', 'result', 'op1', 'op2', max_args=3)
"""
Bitwise AND.
"""
op_xor = subFunction('op', 'xor', 'result', 'op1', 'op2', max_args=3)
"""
Bitwise XOR.
"""
op_not = subFunction('op', 'not', 'result', 'op1', max_args=3)
"""
Bitwise flip.
"""
op_max = subFunction('op', 'max', 'result', 'op1', 'op2', max_args=3)
"""
Maximum of two numbers.
"""
op_min = subFunction('op', 'min', 'result', 'op1', 'op2', max_args=3)
"""
Minimum of two numbers.
"""
op_angle = subFunction('op', 'angle', 'result', 'op1', 'op2', max_args=3)
"""
Angle of vector in degrees.
"""
op_angle_diff = subFunction('op', 'angleDiff', 'result', 'op1', 'op2', max_args=3)
"""
Absolute distance between two angles in degrees.
"""
op_vec_length = subFunction('op', 'len', 'result', 'op1', 'op2', max_args=3)
"""
Length of vector.
"""
op_2d_noise = subFunction('op', 'noise', 'result', 'op1', 'op2', max_args=3)
"""
2D simplex noise.
"""
op_abs = subFunction('op', 'abs', 'result', 'op1', max_args=3)
"""
Absolute value.
"""
op_ln = subFunction('op', 'log', 'result', 'op1', max_args=3)
"""
Natural logarithm (ln).
"""
op_log10 = subFunction('op', 'log10', 'result', 'op1', max_args=3)
"""
Base 10 logarithm.
"""
op_floor = subFunction('op', 'floor', 'result', 'op1', max_args=3)
op_ceil = subFunction('op', 'ceil', 'result', 'op1', max_args=3)
op_sqrt = subFunction('op', 'sqrt', 'result', 'op1', max_args=3)
"""
Square root.
"""
op_randrange = subFunction('op', 'rand', 'result', 'op1', max_args=3)
"""
Random decimal in range [0, value).
"""
op_sin = subFunction('op', 'sin', 'result', 'op1', max_args=3)
"""
Sine, in degrees.
"""
op_cos = subFunction('op', 'cos', 'result', 'op1', max_args=3)
"""
Cosine, in degrees.
"""
op_tan = subFunction('op', 'tan', 'result', 'op1', max_args=3)
"""
Tangent, in degrees.
"""
op_asin = subFunction('op', 'asin', 'result', 'op1', max_args=3)
"""
Arc sine, in degrees.
"""
op_acos = subFunction('op', 'acos', 'result', 'op1', max_args=3)
"""
Arc cosine, in degrees.
"""
op_atan = subFunction('op', 'atan', 'result', 'op1', max_args=3)
"""
Arc tangent, in degrees.
"""


import operator