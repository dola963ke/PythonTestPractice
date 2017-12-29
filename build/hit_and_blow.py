from random import shuffle

def execute():
    N = 4
    a = list(range(1, 10))
    shuffle(a)
    a = ''.join(map(str,a[:N]))
    x = ''
    while x != a:
        hit, blow = 0, 0
        x = input('Input {0} digit number: '.format(N))
        for i, e in enumerate(a):
            if x[i] == e:
                hit += 1
            elif e in x:
                blow += 1
        print('{0} hit, {1} blow'.format(hit, blow))