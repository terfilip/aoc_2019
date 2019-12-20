import operator

class OpCodeThing:

    codes = []
    cur_pos = 0
    halted = False

    # op code dict
    ocd = {
        1: operator.add,
        2: operator.mul
    }

    def __init__(self, in_codes):

        if type(in_codes) == list:
            self.codes = in_codes
        elif type(in_codes) == str:
            self.codes = [int(code) for code in in_codes.split(',')]
        else:
            raise ValueError('wtf')
        
        self.orig_codes = tuple(self.codes)
    
    def reset(self):
        self.halted = False
        self.cur_pos = 0
        self.codes = list(self.orig_codes)

    def do_op(self):

        if self.halted:
            raise ValueError('Halted')

        i = self.cur_pos
        copcode = self.codes[i]

        if copcode == 99:
            self.halted = True
            return
        
        lval = self.codes[self.codes[i + 1]]
        rval = self.codes[self.codes[i + 2]]
        store_pos = self.codes[i + 3]

        self.codes[store_pos] = self.ocd[copcode](lval, rval)
        
        self.cur_pos += 4
    
    def run(self):

        while not self.halted:
            self.do_op()


    def __str__(self):
        i = 0
        out = ''

        while i < len(self.codes):
            if self.codes[i] != 99:

                try:
                    out += ','.join(map(str, self.codes[i:i + 4])) + '\n'
                except IndexError:
                    out += 'ERRR'
                    break
                i += 4
            else:
                out += '99\n'
                i += 1
        
        return out
    
    def __repr__(self):
        return self.__str__()