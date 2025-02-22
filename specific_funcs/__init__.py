from main_functions import (
    _instructions,
    _jump_labels
)
class subFunction:
    def __init__(self, parent_func_name: str, operation_name: str, *arg_names: str, max_args: int | None = None):
        self.name = operation_name
        self.args_ = arg_names
        self.parent_func_name = parent_func_name
        self.max_args = max_args  # subFunction is just a smaller version of Function and this variable is less by 1.

    def __call__(self, *args, jump_instruction_label: str | None = None):
        args = [str(arg) for arg in args]
        if len(args) > self.max_args:
            raise ValueError(f"Too many arguments for function '{self.parent_func_name}.{self.name}'. Expected {self.max_args}, got {len(args)}.")
        if jump_instruction_label != None:
            if jump_instruction_label in _jump_labels:
                raise ValueError(f"Jump label '{jump_instruction_label}' already exists.")
        _jump_labels.add(jump_instruction_label)
        _instructions.append((" ".join([self.parent_func_name, self.name, *args, *["0" for i in (range(self.max_args - len(args)) if self.max_args != None else range(0))]]), jump_instruction_label))

    def __docs__(self):
        return "Arguments: " + ", ".join([*self.args_, *[0 for i in range(self.max_args-len(self.args_))]])
from .mdraw import (
    drawClear,
    drawColor,
    drawCol,
    drawStroke,
    drawLine,
    drawRect,
    drawLineRect,
    drawPoly,
    drawLinePoly,
    drawTriangle,
    drawImage,
    drawPrint,
    drawTranslate,
    drawScale,
    drawRotate,
    drawReset
)
from .mjump import (
    jump_eq,
    jump_neq,
    jump_lt,
    jump_le,
    jump_gt,
    jump_ge,
    jump_seq,
    jump_always
)
from .moperation import (
    op_add,
    op_sub,
    op_mul,
    op_div,
    op_idiv,
    op_mod,
    op_pow,
    op_eq,
    op_neq,
    op_land,
    op_lt,
    op_le,
    op_gt,
    op_ge,
    op_seq,
    op_lshift,
    op_rshift,
    op_or,
    op_and,
    op_xor,
    op_not,
    op_min,
    op_max,
    op_angle,
    op_angle_diff,
    op_vec_length,
    op_2d_noise,
    op_abs,
    op_ln,
    op_log10,
    op_floor,
    op_ceil,
    op_sqrt,
    op_randrange,
    op_sin,
    op_cos,
    op_tan,
    op_asin,
    op_acos,
    op_atan
)
from .mucontrol import (
    control_idle,
    control_stop,
    control_move,
    control_approach,
    control_pathfind,
    control_auto_pathfind,
    control_boost,
    control_target,
    control_targetp,
    control_item_drop,
    control_item_take,
    control_payload_drop,
    control_payload_take,
    control_payload_enter,
    control_mine,
    control_flag,
    control_build,
    control_get_block,
    control_within,
    control_unbind
)