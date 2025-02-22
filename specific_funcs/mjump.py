from . import subFunction


# I am not gonna fix the operation names because I am lazy.


jump_eq = subFunction('jump to', 'equal', 'op1', 'op2', max_args=2)
"""
Equal. Coerces types.
Non-null objects compared with numbers become 1, otherwise 0.
"""
jump_neq = subFunction('jump to', 'notEqual', 'op1', 'op2', max_args=2)
"""
Not equal. Coerces types.
"""
jump_lt = subFunction('jump to', 'lessThan', 'op1', 'op2', max_args=2)
jump_le = subFunction('jump to', 'lessThanEq', 'op1', 'op2', max_args=2)
jump_gt = subFunction('jump to', 'greaterThan', 'op1', 'op2', max_args=2)
jump_ge = subFunction('jump to', 'greaterThanEq', 'op1', 'op2', max_args=2)
jump_seq = subFunction('jump to', 'strictEqual', 'op1', 'op2', max_args=2)
"""
Strict equal. Does not coerce types.

Can be used to check for `null`.
"""
jump_always = subFunction('jump to', 'always', max_args=2)
"""
Always true.
"""