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

Functions that pushes something into the stack.

|Operation|Syntax|Description|
|---|---|---|
|Number|*number*|Will push a number into the stack|
|Rand|`rand`, `random`|Random number between 0 and 1|
|π|`pi`||
|Euler's number|`e`||

### System functions

|Operation|Syntax|Description|
|---|---|---|
|Quit|`q`, `quit`, `exit`|Quits the program|
|Print|`print`, `ls`|Prints the stack|
|Stack show|`ss`, `ts`|Toggles the option to print the full stack at the interactive prompt|

### Stack manipulation and memory

|Operation|Syntax|Description|
|---|---|---|
|Swap|`swp`, `<>`, `><`, `swap`| Swaps the *x* and *y* buffer|
|Roll down|`rld`, `roll`, `rolld`, `rolldown`|Rolls the stack down|
|Roll up|`rlu`, `rollu`, `rollup`|Rolls the stack up|
|Store|`sto`, `store`|Takes one argument that sets the storage location|
|Recall|`rcl`, `recall`|Pushes the numbers stored in an argument position|
|Last X|`lastx`, `lx`|Pushes the value of the *x* buffer before the last calculation|

### Stack drop

Functions that pops off the *x* and *y* buffers and pushes the product based on the function.

|Operation|Syntax|Description|
|---|---|---|
|Add|`a`, `+`, `add`, `plus`||
|Subtract|`s`, `-`, `sub`, `subtact`, `minus`|
|Multiply|`m`, `*`, `mul`, `multiply`, `times`||
|Divide|`d`, `/`, `:`, `div`, `divide`, `over`||
|Power|`p`, `^`, `**`, `pow`, `raised`, `expo`, `exponent`||
|Modulus|`mod`, `modulus`||
|Greatest common divider|`gcd`||
|Logarithm|`log`, `logarithm`|The *x* buffer is the base|
|Root|`r`, `root`|The *x* buffer is the root|

### *x* buffer change

Functions that takes what is stored in the *x* buffer and changes it. Trigonometric functions returns number in radians.

|Operation|Syntax|Description|
|---|---|---|
|Ceil|`cel`, `ceil`||
|Floor|`flr`,`floor`||
|Round|`rnd`, `round`|Rounds to nearest integer|
|Invert|`inv`, `inverse`, `invert`|1 / x|
|Absolute value|`abs`, `absolute`||
|Factorial|`fac`, `factorial`||
|Change sign|`chs`, `changesign`, `chsign`|-x|
|Log base 10|`log10`||
|Log base 2|`log2`||
|Log base e|`ln`, `naturallogarithm`||
|Squareroot|`sqrt`, `squareroot`||
|Sine|`sin`, `sine`||
|Cosine|`cos`, `cosine`||
|Tangent|`tan`, `tangent`||
|Cosecant|`asin`, `arcsin`, `cosecant`||
|Secant|`acos`, `arccos`, `secant`||
|Cotangent|`atan`, `arctan`, `cotangent`||
|Convert to degrees|`deg`, `todeg`, `degrees`||
|Convert to radians|`rad`, `torad`, `radians`||
