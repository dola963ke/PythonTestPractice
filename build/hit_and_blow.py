from random import shuffle

class HitAndBlow:
    def __init__(self, N):
        self.N = N
        self.a = list(range(1, 10))
        self.x = ''

    def _gen_rand(self):
        shuffle(self.a)
        self.a = ''.join(map(str,self.a[:self.N]))

    def _input(self):
        self.x = input('Input {0} digit number: '.format(self.N))

    def _check_and_output(self):
        hit, blow = 0, 0
        for i, e in enumerate(self.a):
            if self.x[i] == e:
                hit += 1
            elif e in self.x:
                blow += 1
        print('{0} hit, {1} blow'.format(hit, blow))

    def execute(self):
        self._gen_rand()
        while self.x != self.a:
            self._input()
            self._check_and_output()
