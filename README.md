# MLogPy (MLog code from Python)
Currently in progress and meant to be used for a game named Mindustry. This is still unfinished. Meant to be used on VSCode.

## How to use
From \_\_init\_\_.py at the outermost folder, create your code at the end of the file, after the `if __name__ == "__main__"`. There is an example there:

```py
if __name__ == "__main__":
    var_result = "result"
    UnitBind(FLARE, jump_instruction_label="jump_to_start")
    Sensor(var_result, UNIT, BLAST_COMPOUND)
    control_unbind()
    Jump("jump_to_start", "equal", var_result, "10")
    UnitLocate(BUILDING, "core", FALSE, COPPER, "outx", "outy", "found", BUILDING)
    control_move("outx", "outy")
    control_item_take(BUILDING, BLAST_COMPOUND, "10")
```
which outputs
```
ubind @flare
sensor result @unit @blast-compound
ucontrol unbind 0 0 0 0 0
jump 0 equal result 10
ulocate building core false @copper outx outy found building
ucontrol move outx outy 0 0 0
ucontrol itemTake building @blast-compound 10 0 0
```

## Upcoming
- A full list of constants, as shorthands for many select object.
- Type.

# Versions
Version 0.1