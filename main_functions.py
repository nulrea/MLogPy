"""
A Python representation to create a Mindustry code for processors.
Meant to be used with VSCode and some editors, as the document will be overwritten.
"""

_instructions: list[tuple[str, str | None]] = []
_jump_labels: set[str] = set()
_output: list[str] = []

def convert_to_text():
    _jump_location: dict[str, int] = {}
    _output.clear()
    for i, (instruction, jump_label) in enumerate(_instructions):
        if jump_label != None:
            _jump_location[jump_label] = i
        
        # if the instruction is a jump
        if instruction.startswith("jump"):
            args = instruction.split(" ")

            if args[1] in _jump_location:
                # if the jump label exists
                args[1] = str(_jump_location[args[1]])
                instruction = " ".join(args)
            else:
                # if not and the jump label is a number
                if all(letter in "0123456789" for letter in args[1]):
                    instruction = " ".join(args)
                else:
                    print(f"Warning: Jump label '{args[1]}' does not exist.")
                    args[1] = "-1"
                    instruction = " ".join(args)
        _output.append(instruction)
    return "\n".join(_output)

class Function:
    """
    A base function class for code.
    Use `__doc__` to get the function's arguments.
    """
    def __init__(self, operation_name: str, *arg_names: str, max_args: int | None = None):
        self.name = operation_name
        self.args_ = arg_names
        self.max_args = max_args

    def __call__(self, *args, jump_instruction_label: str | None = None):
        args = [str(arg) for arg in args]
        if self.max_args == None:
            self.max_args = len(self.args_)
        if len(args) > self.max_args:
            raise ValueError(f"Too many arguments for function '{self.name}'. Expected at most {self.max_args}, got {len(args)}.")
        try:
            if all(letter in "0123456789" for letter in jump_instruction_label):
                raise ValueError("Jump label cannot be a number. Remove this statement by deleting this if statement directly.")
        except TypeError:
            pass
        if jump_instruction_label != None:
            if jump_instruction_label in _jump_labels:
                raise ValueError(f"Jump label '{jump_instruction_label}' already exists.")
        _jump_labels.add(jump_instruction_label)
        _instructions.append((" ".join([self.name, *args, *["0" for i in (range(self.max_args - len(args)) if self.max_args != None else range(0))]]), jump_instruction_label))
    
    def __docs__(self):
        return "Arguments: " + ", ".join(self.args_)

# functions

# i/o
Read = Function('read', 'result', 'cell', 'at')
"""
Read a number from a linked memory cell.
"""
Write = Function('write', 'result', 'cell', 'at')
"""
Write a number from a linked memory cell.
"""
Draw = Function('draw', 'operation_type', 'arg1', 'arg2', 'arg3', 'arg4', 'arg5', 'arg6', max_args=7)
"""
Add an operation to the drawing buffer.

Does not display anything until **Draw Flush** is used.
"""
Print = Function('print', 'string')
"""
Add text to the print buffer.

Does not display anything until **Print Flush** is used.
"""
PrintChar = Function('printchar', 'char')
"""
Add a UTF-16 character or content icon to the print buffer.

Does not display anything until **Print Flush** is used.
"""
Format = Function('format', 'string')
"""
Replace next placeholder in text buffer with a value.

Does not do anything if placeholder pattern is invalid.

Placeholder pattern: `"{number 0-9}"`

Example:
```
print "test {0}"
format "example"
```
"""

# block control
DrawFlush = Function('drawflush', 'to')
"""
Flush queued **Draw** operations to a display.
"""
PrintFlush = Function('printflush', 'to')
"""
Flush queued **Print** operations to a message block.
"""
GetLink = Function('getlink', 'result', 'linknum')
"""
Get a processor link by index. Starts at 0.
"""
Control = Function('control', 'operation_type', 'block', 'arg1', 'arg2', 'arg3')
"""
Control a building.
"""
Radar = Function('radar', 'from', 'operation_type', 'target1', 'target2', 'target3', 'order', 'sort', 'output')
"""
Locate units around a building with range.
"""
Sensor = Function('sensor', 'result', 'attribute', 'block')
"""
Get data from a building or unit.
"""

# operations
Set = Function('set', 'result', 'value')
"""
Set a variable.
"""
Operation = Function('op', 'operation_type', 'result', 'operand1', 'operand2')
"""
Perform an operation on 1-2 variables.
"""
Lookup = Function('lookup', 'result', 'type', 'value')
"""
Look up an item/liquid/unit/block type ID.

Total counts of each type can be accessed with:

`@unitCount`, `@itemCount`, `@liquidCount`, `@blockCount`

For the inverse operation, sense `@id` of the object.
"""
PackColor = Function('packcolor', 'result', 'r', 'g', 'b', 'a')
"""
Pack [0, 1] RBGA components into a single number for drawing or rule-setting.
"""

# control flow
Wait = Function('wait', 'time')
"""
Wait a certain number of seconds.
"""
Stop = Function('stop')
"""
Halt execution of this processor.
"""
End = Function('end')
"""
Jump to the top of the instruction stack.
"""
Jump = Function('jump', 'to', 'operation_type', 'arg1', 'arg2')
"""
Conditionally jump to another statement.
"""

# unit control
UnitBind = Function('ubind', 'type')
"""
Bind to the next unit of a type, and store it in `@unit`.
"""
UnitControl = Function('ucontrol', 'mode', 'arg1', 'arg2', 'arg3', 'arg4', 'arg5')
"""
Control the currently bound unit.
"""
UnitRadar = Function('uradar', 'target1', 'target2', 'target3', 'order', 'sort', 'output')
"""
Locate units around the currently bound unit
"""
UnitLocate = Function('ulocate', 'find', 'group', 'is_enemy', 'ore', 'outX', 'outY', 'found', 'building')
"""
Locate a specific type of position/building anywhere on the map.

Requires a bound unit.
"""