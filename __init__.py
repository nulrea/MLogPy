from main_functions import *
from constants import *
from specific_funcs import (
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
    drawReset,
    jump_eq,
    jump_neq,
    jump_lt,
    jump_le,
    jump_gt,
    jump_ge,
    jump_seq,
    jump_always,
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
    op_atan,
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

if __name__ == "__main__":
    var_result = "result"
    UnitBind(FLARE, jump_instruction_label="jump_to_start")
    Sensor(var_result, UNIT, BLAST_COMPOUND)
    control_unbind()
    Jump("jump_to_start", "equal", var_result, "10")
    UnitLocate(BUILDING, "core", FALSE, COPPER, "outx", "outy", "found", BUILDING)
    control_move("outx", "outy")
    control_item_take(BUILDING, BLAST_COMPOUND, "10")
    # var_remain = 'remain'
    # Sensor(var_remain, TITANIUM, 'nucleus1')
    # Jump(4, 'greaterThan', var_remain, 1000)
    # Control('enabled', 'conveyor2', 0)
    # End()
    # Control('enabled', 'conveyor2', 1)
    # end
    code = convert_to_text()
    print(code)