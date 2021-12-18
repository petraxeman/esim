import settings
import random as rnd


class Tree:
    def __init__(self, position, dna) -> None:
        self.position = position
        self.dna = dna

class DNA:
    def __init__(self, code = None):
        if code is None:
            code = DNA.generate_code()
        self.code = code
    def get_specific_gen(self, num):
        return self.code[num]
    def division(self):
        if rnd.randint(0, 100) <= settings.mutation_chance:
            mutated_gen_num = rnd.randint(0, settings.dna_code_rows - 1)
            mutated_gen = list(self.get_specific_gen(mutated_gen_num))
            print(mutated_gen, end = '')
            mutated_gen[rnd.randint(0, settings.dna_row_symbols - 1)] = rnd.randint(0, settings.dna_max_symobl)
            print('  ', mutated_gen)
            return 1
        else:
            print('Mutation failed :(')
            return 0
    @classmethod
    def generate_code(cls):
        code = tuple([tuple([rnd.randint(0, settings.dna_max_symobl) for z in range(settings.dna_row_symbols)]) for i in range(settings.dna_code_rows)])
        return code

d = DNA()
s = 0
f = 0
for i in range(10000):
    a = d.division()
    if a == 1:
        s += 1
    else:
        f += 1

print('Succes:', s, 'Failed:', f)
