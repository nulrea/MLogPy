from . import subFunction


control_idle = subFunction('ucontrol', 'idle', max_args=5)
"""
Don't move, but keep building/mining.

The default state.
"""
control_stop = subFunction('ucontrol', 'stop', max_args=5)
"""
Stop moving/mining/building.
"""
control_move = subFunction('ucontrol', 'move', 'x', 'y', max_args=5)
"""
Move to exact location.
"""
control_approach = subFunction('ucontrol', 'approach', 'x', 'y', 'radius', max_args=5)
"""
Approach a position with a radius.
"""
control_pathfind = subFunction('ucontrol', 'pathfind', 'x', 'y', max_args=5)
"""
Pathfind to the specific position.
"""
control_auto_pathfind = subFunction('ucontrol', 'autoPathfind', max_args=5)
"""
Automatically pathfinds to the nearest enemy core or drop point.

This is the same as standard wave enemy spawning.
"""
control_boost = subFunction('ucontrol', 'boost', 'is_enabled', max_args=5)
"""
Start/stop boosting.
"""
control_target = subFunction('ucontrol', 'target', 'x', 'y', 'shoot', max_args=5)
"""
Shoot a position.
"""
control_targetp = subFunction('ucontrol', 'targetp', 'target', 'shoot', max_args=5)
"""
Shoot a target with velocity prediction.
"""
control_item_drop = subFunction('ucontrol', 'itemDrop', 'to', 'amount', max_args=5)
"""
Drop an item.
"""
control_item_take = subFunction('ucontrol', 'itemTake', 'from', 'item', 'amount', max_args=5)
"""
Take an item from a building.
"""
control_payload_drop = subFunction('ucontrol', 'payDrop', max_args=5)
"""
Drop current payload.
"""
control_payload_take = subFunction('ucontrol', 'payTake', 'takeUnits', max_args=5)
"""
Pick up payload at current location.
"""
control_payload_enter = subFunction('ucontrol', 'payEnter', max_args=5)
"""
Enter/land on the payload block the unit is on.
"""
control_mine = subFunction('ucontrol', 'mine', 'x', 'y', max_args=5)
"""
Mine at a position.
"""
control_flag = subFunction('ucontrol', 'flag', 'value', max_args=5)
"""
Numeric unit flag.
"""
control_build = subFunction('ucontrol', 'build', 'x', 'y', 'block', 'rotation', 'config', max_args=5)
"""
Build a structure.
"""
control_get_block = subFunction('ucontrol', 'getBlock', 'x', 'y', 'type', 'building', 'floor', max_args=5)
"""
Fetch building, floor and block type at coordinates.


Unit must be in range of the position, otherwise `null` is returned.
"""
control_within = subFunction('ucontrol', 'within', 'x', 'y', 'radius', 'result', max_args=5)
"""
Check if unit is near a position.
"""
control_unbind = subFunction('ucontrol', 'unbind', max_args=5)
"""
Completely disable logic control.

Resume standard AI.
"""
