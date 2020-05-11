

class DinoInterp:


    def __init__(self,prog):
        self.prog = prog
        self.vars = {}


    def readData(self):
        for sentno in self.prog:
            print(sentno, self.prog[sentno])

    def run(self):
        print("Output:")
        print()
        for sentno in self.prog:
            type = self.prog[sentno][0]                           #luis is a/an tall. luis is a person          luis: tall, 24
            if type == 'definition':
                print(str(sentno) + ":", self.define(self.prog[sentno][1]))
            elif type == 'question':
                print(str(sentno) + ":", self.relate(self.prog[sentno][1]))
            elif type == 'modification':
                print(str(sentno) + ":", self.modify(self.prog[sentno][1]))
            else: #expression
                print(str(sentno) + ":", self.prog[sentno][1])
        print()
        print('variables:')
        print(self.vars)

    def define(self,sentence):
        key, value = sentence
        if isinstance(value,list):
            self.vars[key] = {'value':value , 'len':len(value)}
            return self.vars[key]
        elif isinstance(value,int) or isinstance(value,bool):
            self.vars[key] = value
            return self.vars[key]
        else:
            self.vars[key] = {'value':value }
            return self.vars[key]

    def relate(self,sentence):
        key = 0
        value = None

        if len(sentence) == 2:
            key, value = sentence
        else:
            key = sentence

        if not value:
            if key in self.vars.keys():
                return self.vars[key]['value']
            else:
                return None
        else:
            if key in self.vars.keys() and isinstance(self.vars[key],dict) and value in self.vars[key].keys():
                return self.vars[key][value]
            else:
                return None

    def modify(self, sentence):
        key = sentence[0]
        char, value = sentence[1]
        if key in self.vars.keys():
            self.vars[key][char] = value
            return True
        else:
            return False
