"""
A Python representation to create a Mindustry code for processors.
Meant to be used with VSCode and some editors, as the document will be overwritten.

version 0.0.2 | developing stage
"""

from typing import Any, Literal
from constants import _UnitType, _SortType, _LookupType, _BuildingType
from constants import *


_instructions: list[tuple[str, str | None]] = []
_jump_labels: set[str] = set()
_output: list[str] = []

class String:
    def __init__(self, str_: Any):
        self.str_ = str(str_)

    def __str__(self):
        return f'"{self.str_}"'

def convert_to_text():
    _jump_location: dict[str, int] = {}
    _output.clear()
    for i, (instruction, jump_label) in enumerate(_instructions):
        if jump_label != None:
            _jump_location[jump_label] = i
        args = instruction.split(" ")
        
        # if the instruction is a jump
        if instruction.startswith("jump"):
            if len(args) == 0:
                if args[1] in _jump_location:
                    # if the jump label exists
                    args[1] = str(_jump_location[args[1]])
                else:
                    print(f"Warning: Jump label '{args[1]}' does not exist.")
                    args[1] = "-1"
        instruction = " ".join(args) if instruction.startswith("jump") else instruction
        print(instruction)
        _output.append(instruction)
    return "\n".join(_output)

def func(*args, jump_instruction_label, **kwargs) -> None:
    try:
        if all(letter in "0123456789" for letter in jump_instruction_label):
            raise ValueError("Jump label cannot be a number. Remove this statement by deleting this if statement directly.")
    except TypeError:
        pass
    if args.__len__ == 0:
        raise ValueError("Instruction cannot be empty.")
    if jump_instruction_label != None:
        if jump_instruction_label in _jump_labels:
            raise ValueError(f"Jump label '{jump_instruction_label}' already exists.")
    _jump_labels.add(jump_instruction_label)
    _instructions.append((" ".join([str(i) for i in [*args, *(kwargs.values())]]), jump_instruction_label))

# functions

# i/o
def Read(
        result_var = 'result', 
        to = 'cell1', 
        at = 0, 
        *, 
        jump_label = None) -> None:
    """
    Read a number from a linked memory cell.

    Parameters
    ----------
    result_var : variable_name
        Variable name to store the result.
    
    to : structure_name
        Cell to read from.

    at : int
        Cell (data location) to read from.
    """
    func('read', result_var, to, at, jump_instruction_label=jump_label)
def Write(
        result_var = 'result', 
        to = 'cell1', 
        at = 0, 
        *, 
        jump_label = None) -> None:
    """
    Write a number from a linked memory cell.

    Parameters
    ----------
    result_var : variable_name
        Variable name to write the result.
    
    to : structure_name
        Cell to write.

    at : int
        Cell (data location) to write to.
    """
    func('write', result_var, to, at, jump_instruction_label=jump_label)
def Draw(
        op='clear', 
        arg1 = 0, 
        arg2 = 0, 
        arg3 = 0, 
        arg4 = 0, 
        arg5 = 0, 
        arg6 = 0, 
        *, 
        jump_label = None) -> None:
    """
    Add an operation to the drawing buffer.

    Does not display anything until **DrawFlush** is used.

    Parameters
    ----------
    op : op_name
        Operation to do.
    
    arg1~6 : any
        Arguments to apply. Any unusued argument should be left 0.
    """
    func('draw', op, arg1, arg2, arg3, arg4, arg5, arg6, jump_instruction_label=jump_label)
def Print(
        string: str | String = String('frog'),
        *, 
        jump_label = None
        ) -> None:
    """
    Add text to the print buffer.

    Does not display anything until **PrintFlush** is used.

    Parameters
    ----------
    string : str | String
        String to print.
    """
    func('print', string, jump_instruction_label=jump_label)
def PrintChar(
        char = 65,
        *, 
        jump_label = None
        ) -> None:
    """
    Add a UTF-16 character or content icon to the print buffer.

    Does not display anything until **PrintFlush** is used.
    """
    func('printchar', char, jump_instruction_label=jump_label)
def Format(
        string: str | String = String('frog'),
        *, 
        jump_label = None
        ) -> None:
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
    func('format', string, jump_instruction_label=jump_label)
# block control
def DrawFlush(
        to='display1',
        *, 
        jump_label = None
        ) -> None:
    """
    Flush queued **Draw** operations to a display.
    """
    func('drawflush', to, jump_instruction_label=jump_label)
def PrintFlush(
        to='message1',
        *, 
        jump_label = None
        ) -> None:
    """
    Flush queued **Print** operations to a message block.
    """
    func('printflush', to, jump_instruction_label=jump_label)
def GetLink(
        result_var = 'result', 
        linknum: int = 0,
        *, 
        jump_label = None
        ) -> None:
    """
    Get a processor link by index. Starts at 0.
    """
    func('getlink', result_var, linknum, jump_instruction_label=jump_label)
def Control(
        op_type = 'enabled', 
        block = 'block1', 
        arg1 = 0, 
        arg2 = 0, 
        arg3 = 0,
        *, 
        jump_label = None
        ) -> None:
    """
    Control a building.
    """
    func('control', op_type, block, arg1, arg2, arg3, jump_instruction_label=jump_label)
def Radar(
        from_ = 'turret1', 
        target1: _UnitType = 'enemy', 
        target2: _UnitType = 'any', 
        target3: _UnitType = 'any', 
        order: Literal[0, 1] = 1, 
        sort: _SortType = 'distance', 
        output_var = 'result',
        *, 
        jump_label = None
        ) -> None:
    """
    Locate units around a building with range.
    """
    func('radar', target1, target2, target3, sort, from_, order, output_var, jump_instruction_label=jump_label)
def Sensor(
        result_var = 'result', 
        attribute = COPPER, 
        block = 'block1',
        *, 
        jump_label = None
        ) -> None:
    """
    Get data from a building or unit.
    """
    func('sensor', result_var, block, attribute, jump_instruction_label=jump_label)
# operations
def Set(
        var, 
        value,
        *, 
        jump_label = None
        ) -> None:
    """
    Set a variable.
    """
    func('set', var, value, jump_instruction_label=jump_label)
def Operation(
        result_var = 'result', 
        op = 'add', 
        operand1 = 'a', 
        operand2 = 'b',
        *, 
        jump_label = None
        ) -> None:
    """
    Perform an operation on 1-2 variables.
    """
    func('op', op, result_var, operand1, operand2, jump_instruction_label=jump_label)
def Lookup(
        result_var = 'result', 
        type_: _LookupType = 'item', 
        id: int = 0,
        *, 
        jump_label = None
        ) -> None:
    """
    Look up an item/liquid/unit/block type ID.

    Total counts of each type can be accessed with:

    `@unitCount`, `@itemCount`, `@liquidCount`, `@blockCount`

    For the inverse operation, sense `@id` of the object.
    """
    func('lookup', type_, result_var, id, jump_instruction_label=jump_label)
def PackColor(
        result_var = 'result', 
        r: float = 1, 
        g: float = 0, 
        b: float = 0, 
        a: float = 1,
        *, 
        jump_label = None
        ) -> None:
    """
    Pack [0, 1] RBGA components into a single number for drawing or rule-setting.
    """
    func('packcolor', result_var, r, g, b, a)

# control flow
def Wait(
        duration: float = 0.5,
        *, 
        jump_label = None        
        ) -> None:
    """
    Wait a certain number of seconds.
    """
    func('wait', duration, jump_instruction_label=jump_label)
def Stop(
        *, 
        jump_label = None  
        ) -> None:
    """
    Halt execution of this processor.
    """
    func('stop', jump_instruction_label=jump_label)
def End(
        *, 
        jump_label = None  
        ) -> None:
    """
    Jump to the top of the instruction stack.
    """
    func('end', jump_instruction_label=jump_label)
def Jump(
        to: int | str = -1,
        op = 'notEqual',
        operand1 = 'x',
        operand2 = 'false',
        *, 
        jump_label = None  
        ) -> None:
    """
    Conditionally jump to another statement.
    """
    func('jump', to, op, operand1, operand2, jump_instruction_label=jump_label)

# unit control
def UnitBind(
        type_ = POLY,
        *, 
        jump_label = None  
        ) -> None:
    """
    Bind to the next unit of a type, and store it in `@unit`.
    """
    func('ubind', type_, jump_instruction_label=jump_label)
def UnitControl(
        mode = 'move', 
        arg1 = 0, 
        arg2 = 0, 
        arg3 = 0, 
        arg4 = 0, 
        arg5 = 0,
        *, 
        jump_label = None
        ) -> None:
    """
    Control the currently bound unit.
    """
    func('ucontrol', mode, arg1, arg2, arg3, arg4, arg5, jump_instruction_label=jump_label)
def UnitRadar(
        target1: _UnitType = 'enemy', 
        target2: _UnitType = 'any', 
        target3: _UnitType = 'any', 
        order: Literal[0, 1] = 1, 
        sort: _SortType = 'distance', 
        result_var = 'result',
        *, 
        jump_label = None
        ) -> None:
    """
    Locate units around the currently bound unit
    """
    func('uradar', target1, target2, target3, 0, sort, result_var)
def UnitLocate(
        find: _BuildingType = BUILDING, 
        group = 'core', 
        is_enemy = 'true', 
        ore = COPPER, 
        result_var_X = 'outx', 
        result_var_Y = 'outy', 
        found = 'found', 
        building = 'building') -> None:
    """
    Locate a specific type of position/building anywhere on the map.

    Requires a bound unit.
    """
    func('ulocate', find, group, is_enemy, ore, result_var_X, result_var_Y, found, building)