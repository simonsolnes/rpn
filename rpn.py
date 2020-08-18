#!/usr/bin/env python3
import re
import math
import sys
import random

show_full_stack=False
showed_stack=False

class Stack():
    def __init__(self):
        self.list = []
        self.lastx = float(0)
    def push(self, item):
        if len(self.list) < 1 and item == 0:
            return
        self.list.insert(0, item)
    def pop(self):
        if not self:
            return float(0)
        retval = self.list[0]
        self.list = self.list[1:]
        return retval
    def drop(self, func):
        x = self.pop()
        self.lastx = x
        y = self.pop()
        try:
            self.push(func(x, y))
        except Exception as e:
            print(e)
            self.push(x)
            self.push(y)
    def change(self, func):
        self.lastx = self.list[0]
        self.push(func(self.pop()))
    def __getitem__(self, key):
        if type(key) == slice: raise IndexError('No stack slicing')
        if key == 0: raise IndexError('There exsist no index 0')
        if key == 'x': idx = 0
        elif key == 'y': idx = 1
        else: idx = key + 1
        if (idx == 0 and len(self) < 1) or (idx == 1 and len(self) < 2):
            return float(0)
        if idx > len(self): raise IndexError('Index out of stack range')
        return float(self.list[idx])
    def __setitem__(self, key, value):
        if type(key) == slice: raise IndexError('No stack slicing')
        if key == 0: raise IndexError('There exsist no index 0')
        if key == 'x': idx = 0
        elif key == 'y': idx = 1
        else: idx = key + 1
        if idx > len(self): raise IndexError('Index out of stack range')
        if not (idx == 0 and len(self) < 1) or (idx == 1 and len(self) < 2):
            self.list[idx] = value
        
    def gettable(self):
        stack = list(self.list)
        while len(stack) < 2:
            stack.append(float(0))
        labelstack = []
        for idx, num in enumerate(stack):
            if idx == 0: reg = ' x'
            elif idx == 1: reg = ' y'
            else: reg = str(idx - 1)
            if len(reg) < 2: reg = ' ' + reg
            labelstack.append([reg, num])
        return labelstack[::-1]
    def roll(self, direction = 0):
        if len(self.list) < 1:
            return

        if len(self.list) == 1:
            self.list.append(float(0))
        if direction == 0:
            self.list = self.list[1:] + self.list[:1]
        elif direction == 1:
            self.list = self.list[-1:] + self.list[:-1]
    def __len__(self):
        return len(self.list)
            
class RPN():
    def __init__(self):
        self.stack = Stack()
        self.regtable = {}
    def setdefault(self):
        self.angle = 'deg'

    def exe(self, raw):
        global showed_stack, show_full_stack
        ln = iter(raw.split(' '))
        for cmd in ln:
            if re.search('^-?(\d+\.?\d*|\.\d+)$', cmd):
                self.stack.push(float(cmd))

            # drop
            elif cmd in ['a', '+', 'add', 'plus']:
                self.stack.drop(lambda x, y: y + x)
            elif cmd in ['s', '-', 'sub', 'subtact', 'minus']:
                self.stack.drop(lambda x, y: y - x)
            elif cmd in ['m', '*', 'mul', 'multiply', 'times']: # * doesn't work
                self.stack.drop(lambda x, y: y * x)
            elif cmd in ['d', '/', ':', 'div', 'divide', 'over']:
                self.stack.drop(lambda x, y: y / x)
            elif cmd in ['p', '^', '**', 'pow', 'raised', 'expo', 'exponent']:
                self.stack.drop(lambda x, y: math.pow(y, x))
            elif cmd in ['mod', 'modulus']:
                self.stack.drop(lambda x, y: math.fmod(y, x))
            elif cmd in ['gcd']:
                self.stack.drop(lambda x, y: math.gcd(y, x))
            elif cmd in ['log', 'logarithm']:
                self.stack.drop(lambda x, y: math.log(y, x))
            elif cmd in ['r', 'root']:
                self.stack.drop(lambda x, y: math.pow(y, 1/x))

            # change
            elif cmd in ['cel', 'ceil']:
                self.stack.change(lambda x: math.ceil(x))
            elif cmd in ['flr','floor']:
                self.stack.change(lambda x: math.floor(x))
            elif cmd in ['rnd', 'round']:
                self.stack.change(lambda x: round(float(x)))
            elif cmd in ['inv', 'inverse', 'invert']:
                self.stack.change(lambda x: 1 / x)
            elif cmd in ['abs', 'absolute']:
                self.stack.change(lambda x: math.fabs(x))
            elif cmd in ['fac', 'factorial']:
                self.stack.change(lambda x: math.factorial(x))
            elif cmd in ['chs', 'changesign', 'chsign']:
                self.stack.change(lambda x: -x)
            elif cmd in ['log10']:
                self.stack.change(lambda x: math.log10(x))
            elif cmd in ['log2']:
                self.stack.change(lambda x: math.log2(x))
            elif cmd in ['ln', 'naturallogarithm']:
                self.stack.change(lambda x: math.log(x))
            elif cmd in ['sqrt', 'squareroot']:
                self.stack.change(lambda x: math.sqrt(x))
            elif cmd in ['sin', 'sine']:
                self.stack.change(lambda x: math.sin(x))
            elif cmd in ['cos', 'cosine']:
                self.stack.change(lambda x: math.cos(x))
            elif cmd in ['tan', 'tangent']:
                self.stack.change(lambda x: math.tan(x))
            elif cmd in ['asin', 'arcsin', 'cosecant']:
                self.stack.change(lambda x: math.asin(x))
            elif cmd in ['acos', 'arccos', 'secant']:
                self.stack.change(lambda x: math.acos(x))
            elif cmd in ['atan', 'arctan', 'cotangent']:
                self.stack.change(lambda x: math.atan(x))
            elif cmd in ['deg', 'todeg', 'degrees']:
                self.stack.change(lambda x: math.degrees(x))
            elif cmd in ['rad', 'torad', 'radians']:
                self.stack.change(lambda x: math.radians(x))

            # generative
            elif cmd in ['rand', 'random']:
                self.stack.push(random.uniform(0, 1))
            elif cmd in ['pi']:
                self.stack.push(math.pi)
            elif cmd in ['e']:
                self.stack.push(math.e)

            # system
            elif cmd in ['q', 'quit', 'exit']:
                exit(0)
            elif cmd in ['print', 'ls']:
                for item in self.stack.gettable():
                    print(item[0] + ': ' + InteractiveMode().prettify(item[1]))
                    showed_stack=1
            elif cmd in ['ss', 'ts']:
                show_full_stack = not show_full_stack

            # functions
            elif cmd in ['swp', '<>', '><', 'swap']:
                self.stack['x'], self.stack['y'] = self.stack['y'], self.stack['x']
            elif cmd in ['rld', 'roll', 'rolld', 'rolldown']:
                self.stack.roll()
            elif cmd in ['rlu', 'rollu', 'rollup']:
                self.stack.roll(1)
            elif cmd in ['sto', 'store']:
                self.regtable[next(ln)] = self.stack['x']
            elif cmd in ['rcl', 'recall']:
                self.stack.push(self.regtable[next(ln)])
            elif cmd in ['clr', 'clear', 'clean', 'erase']:
                self.stack = Stack()
            elif cmd in ['dup']:
                x=self.stack.pop()
                self.stack.push(x)
                self.stack.push(x)
            elif cmd in ['lastx', 'lx']:
                last=self.stack.lastx
                self.stack.push(last)
            elif cmd in '':
                pass
            else:
                
                raise Exception('invalid command')

        return int(self.stack['x']) if self.stack['x'].is_integer() else self.stack['x']

class InteractiveMode():
    def __init__(self):
        self.rpn = RPN()

    def run(self):
        global showed_stack, show_full_stack
        while True:
            if not showed_stack:
                if show_full_stack:
                    self.rpn.exe('ls')
                else:
                    print('\x1b[2m x: \x1b[0m' + self.prettify(self.rpn.stack['x']))
            showed_stack=False
            try:
                ret = self.rpn.exe(input(' > '))
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                print()
                for item in self.rpn.stack.gettable():
                    print(item[0] + ': ' + self.prettify(item[1]))
                exit()
    def run2(self):
        try:
            import sys, tty, termios
        except ImportError:
            try:
                import msvcrt
            except ImportError:
                raise ImportError('getch not available')
            else:
                getch = msvcrt.getch
        else:
            def getch():
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch

        def keypress(key):
            if ord(key) == 13: #enter
                print(end='\r')
                try:
                    self.rpn.exe(self.buffer)
                except Exception as e:
                    print(e)
                finally:
                    print(' ' + self.prettify(self.rpn.stack['x']), end='\r')
                    self.buffer = ''
            else:
                if ord(key) == 3: # ^C
                    print()
                    exit()
                elif ord(key) == 127: # backspace
                    self.buffer = self.buffer[:-1]
                else:
                    self.buffer += key
                print(' ' * 80 + '\r ' + self.buffer, end='\r')

        self.buffer = ''
        print(' ' + self.prettify(self.rpn.stack['x']), end='\r')
        while True:
            keypress(getch())

    def prettify(self, num):
        if num >= 0:
            number = ' %015.4f' % float(num)
        else:
            number = '%016.4f' % float(num)
        sign = number[0]
        formated = [ch for ch in number[1:]]
        for idx, ch in enumerate(formated):
            if ch == '0': formated[idx] = '\x1b[2m0\x1b[0m'
            else: break
        formated = formated[::-1]
        for idx, ch in enumerate(formated):
            if ch == '0': formated[idx] = '\x1b[2m0\x1b[0m'
            else: break
        formated = formated[::-1]
        if num.is_integer():
            for idx, ch in enumerate(formated):
                if ch == '.': formated[idx] = '\x1b[2m.\x1b[0m'
            
        return sign + ''.join(formated)
            
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(RPN().exe(' '.join(sys.argv[1:])))
    else:
        InteractiveMode().run()
