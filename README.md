# Command-Line RPN calculator

Command line tools that can take an expression as arguments or interactively.

![Screenshot](https://github.com/simonsolnes/rpn/raw/master/screenshot.png)

## General
The program takes inputs that are separated by space (or return in interactive mode). Inputs can be either numbers or a function. Functions can be stack manipulation or all of the common mathematical operations.

### Examples
- **2 + (-5)**: `2 -5 add`
- **3 / -1**: `3 1 chs div`
- **sqrt(9)^cos(3.4)**: `9 2 root 3.4 cos pow`

## Functions

### Stack pushes

Funcions that pushes something into the stack.

|Operation|Syntax|Description|
|---|---|---|
|Number|*number*|Will push a number into the stack|
|Rand|`rand`, `random`|Random number between 0 and 1|
|π|`pi`||
|Euler's number|`e`||

### System funcions

|Operation|Syntax|Description|
|---|---|---|
|Quit|'q', 'quit', 'exit'|Quits the program|
|Print|'print', 'ls', 'p'|Prints the stack|

### Stack manipulation and memory

|Operation|Syntax|Description|
|---|---|---|
|Swap|`swp`, `<>`, `><`, `swap`| Swaps the *x* and *y* buffer|
|Roll down|'rld', 'roll', 'rolld', 'rolldown'|Rolls the stack down|
|Roll up|'rlu', 'rollu', 'rollup'|Rolls the stack up|
|Store|'sto', 'store'|Takes one argument that sets the storage location|
|Recall|'rcl', 'recall'|Pushes the numbes stored in a argument position|
