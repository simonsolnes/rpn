#!/usr/bin/env python3
import re
import math
import sys

class Err(str):
    pass

class Info(str):
    pass

class Stack():
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.insert(0, item)
    def pop(self):
        if not self:
            return 0
        retval = self.list[0]
        self.list = self.list[1:]
        return retval
    def drop(self, func):
        x = self.pop()
        y = self.pop()
        self.push(func(x, y))
    def change(self, func):
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
        return self.list[idx]
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
    def __len__(self):
        return len(self.list)
            
class RPN():
    def __init__(self):
        self.stack = Stack()
        self.regtable = {}
    def setdefault(self):
        self.angle = 'deg'

    def cmd_util(self):
        while True:
            print('\x1b[2m x: \x1b[0m' + self.prettify(self.stack['x']) + ' > ', end='')
            ret = self.exe(input())
            if isinstance(ret, Err) or isinstance(ret, Info):
                print(ret)

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

    def exe(self, raw):
        if raw == '':
            return

        ln = iter(raw.split(' '))
        for cmd in ln:
            if re.search('^-?\d*\.?\d*$', cmd):
                self.stack.push(float(cmd))

            elif cmd in ['+', 'a', 'add', 'plus']:
                self.stack.drop(lambda x, y: y + x)
            elif cmd in ['-', 's', 'sub', 'subtact', 'minus']:
                self.stack.drop(lambda x, y: y - x)
            elif cmd in ['*', 'm', 'mul', 'multiply', 'times']:
                self.stack.drop(lambda x, y: y * x)
            elif cmd in ['/', 'd', 'div', 'divide', 'over']:
                self.stack.drop(lambda x, y: y / x)
            elif cmd in ['q', 'quit', 'exit']:
                exit(0)

            elif cmd == 'ceil':
                self.stack.change(lambda x: math.ceil(x))
            elif cmd == 'floor':
                self.stack.change(lambda x: math.floor(x))
            elif cmd == 'abs':
                self.stack.change(lambda x: math.fabs(x))
            elif cmd == 'factorial':
                self.stack.change(lambda x: math.factorial(x))
            elif cmd == 'mod':
                self.stack.drop(lambda x, y: math.fmod(y, x))
            elif cmd in ['print', 'ls', 'p']:
                for item in self.stack.gettable():
                    print(item[0] + ': ' + self.prettify(item[1]))

            # one argument functions
            elif cmd == 'sto':
                self.regtable[next(ln)] = self.stack['x']
            elif cmd == 'rcl':
                self.stack.push(self.regtable[next(ln)])

            else:
                return Err('invalid command')

        return int(self.stack['x']) if self.stack['x'].is_integer() else self.stack['x']

            
if __name__ == "__main__":
    rpn = RPN()
    if len(sys.argv) > 1:
        print(rpn.exe(' '.join(sys.argv[1:])))
    else:
        rpn.cmd_util()
