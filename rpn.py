import re
import math

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
            return 0
        if idx > len(self): raise IndexError('Index out of stack range')
        return self.list[idx]
    def __repr__(self):
        retval = ''
        stack = list(self.list)
        while len(stack) < 2:
            stack.append(0)
        labelstack = []
        for idx, num in enumerate(stack):
            if idx == 0: reg = ' x'
            elif idx == 1: reg = ' y'
            else: reg = str(idx - 1)
            if len(reg) < 2: reg = ' ' + reg
            if num >= 0: labelstack.append(reg + ':  ' + '%010.4f' % num)
            else: labelstack.append(reg + ': ' + '%011.4f' % num)
        return '\n'.join(labelstack[::-1])
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
            if self.stack['x'] >= 0:
                number = ' %010.4f' % float(self.stack['x'])
            else:
                number = '%011.4f' % float(self.stack['x'])
            print(number + ' > ', end='')
            ret = self.exe(input())
            if isinstance(ret, Err) or isinstance(ret, Info):
                print(ret)

    def exe(self, raw):
        if raw == '':
            return

        i = 0
        ln = raw.split(' ')
        while i < len(ln):

    ### Zero arg cmds
        # Arithmetic
            if re.search('^(a|add|\+)$', ln[i]):
                self.stack.drop(lambda x, y: y + x)
            elif re.search('^(s|sub|subtact|\-)$', ln[i]):
                self.stack.drop(lambda x, y: y - x)
            elif re.search('^(f|m|mul|multiply|\*)$', ln[i]):
                self.stack.drop(lambda x, y: y * x)
            elif re.search('^(d|div|divide|\/)$', ln[i]):
                self.stack.drop(lambda x, y: y / x)
            elif re.search('^(q|quit|exit)$', ln[i]):
                exit(0)

            elif ln[i] == 'ceil':
                self.stack.change(lambda x: math.ceil(x))
            elif ln[i] == 'floor':
                self.stack.change(lambda x: math.floor(x))
            elif ln[i] == 'abs':
                self.stack.change(lambda x: math.fabs(x))
            elif ln[i] == 'factorial':
                self.stack.change(lambda x: math.factorial(x))

            elif ln[i] == 'mod':
                self.stack.drop(lambda x, y: math.fmod(y, x))
        # Print
            elif ln[i] == 'print':
                return Info(self.stack)
    ### One arg cmds
            elif ln[i] in ['sto', 'rcl']:
            # STO
                if i + 1 > len(ln):
                    return Err(ln[i] + ' requires exaclyt one argument')
                if ln[i] == 'sto':
                    self.regtable[ln[i + 1]] = self.stack['x']
            # RCL
                elif ln[i] == 'rcl':
                    self.stack.push(self.regtable[ln[i + 1]])

                i += 1

    ### Number
            elif re.search('^-?\d*\.?\d*$', ln[i]):
                self.stack.push(float(ln[i]))
            else:
                return Err('invalid command')
            i += 1

        return self.stack['x']
            
if __name__ == "__main__":
    rpn = RPN()
    rpn.cmd_util()
