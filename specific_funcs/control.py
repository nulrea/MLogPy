from . import subFunction


controlEnabled = subFunction("control", "enabled", 'block', 'is_enabled', max_args=4)
"""
Whether the block is enabled.
"""
controlShoot = subFunction("control", "shoot", 'block', 'x', 'y', 'shoot', max_args=4)
"""
Shoot at a position.
"""
controlShootPrediction = subFunction("control", "shootp", 'block', 'aim_to', 'shoot', max_args=4)
"""
Shoot at a unit/building with velocity prediction.
"""
controlConfig = subFunction("control", "config", 'block', 'value', max_args=4)
"""
Building configuration, e.g. sorter item.
"""
controlColor = subFunction("control", "color", 'block', 'value', max_args=4)
"""
Illuminating color.
"""