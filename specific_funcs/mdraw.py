from . import subFunction


drawClear = subFunction("draw", "clear", 'r', 'g', 'b', max_args=6)
"""
Fill a display with a color.
"""
drawColor = subFunction("draw", "color", 'r', 'g', 'b', 'a', max_args=6)
"""
Set the color for next drawing operations.
"""
drawCol = subFunction("draw", "col", 'color', max_args=6)
"""
Equivalent to `drawColor`, but packed.

Packed colors are written as hex codes with a `%` prefix.

Example: `%ff0000` would be red.
"""
drawStroke = subFunction("draw", "stroke", 'width', max_args=6)
"""
Set line width.
"""
drawLine = subFunction("draw", "line", 'x1', 'y1', 'x2', 'y2', max_args=6)
"""
Draw line segment.
"""
drawRect = subFunction("draw", "rect", 'x', 'y', 'width', 'height', max_args=6)
"""
Fill a rectangle.
"""
drawLineRect = subFunction("draw", "lineRect", 'x', 'y', 'width', 'height', max_args=6)
"""
Draw a rectangle outline.
"""
drawPoly = subFunction("draw", "poly", 'x', 'y', 'sides', 'radius', 'rotation', max_args=6)
"""
Fill a regular polygon.
"""
drawLinePoly = subFunction("draw", "linePoly", 'x', 'y', 'sides', 'radius', 'rotation', max_args=6)
"""
Draw a regular polygon outline.
"""
drawTriangle = subFunction("draw", "triangle", 'x', 'y', 'x2', 'y2', 'x3', 'y3', max_args=6)
"""
Fill a triangle.
"""
drawImage = subFunction("draw", "image", 'x', 'y', 'image', 'size', 'rotation', max_args=6)
"""
Draw an image of some content.

ex: `@router` or `@dagger`.
"""
drawPrint = subFunction("draw", "print", 'x', 'y', 'align', max_args=6)
"""
Draws text from the print buffer.

Only ASCII characters are allowed.

Clears the print buffer.
"""
drawTranslate = subFunction("draw", "translate", 'x', 'y', max_args=6)
drawScale = subFunction("draw", "scale", 'x', 'y', max_args=6)
drawRotate = subFunction("draw", "rotate", 'degrees', max_args=6)
drawReset = subFunction("draw", "reset", max_args=6)