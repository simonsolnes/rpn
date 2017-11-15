# Command-Line RPN calculator

Command line tools that can take an expression as arguments or interactively.

![Screenshot](https://github.com/simonsolnes/rpn/raw/master/screenshot.png)

## General guide
The program takes inputs that are separated by space (or return in interactive mode). Inputs can be either numbers or a function. Functions can be stack manipulation or all of the common mathematical operations.

### Examples
- **2 + (-5)**: `2 -5 add`
- **3 / -1**: `3 1 chs div`
- **sqrt(9)^cos(3.4)**: `9 2 root 3.4 cos pow`
