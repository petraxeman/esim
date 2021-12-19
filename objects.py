import settings
import random as rnd


class Tree:
    def __init__(self, position, dna = 0) -> None:
        self.position = position
        self.dna = dna if dna else DNA()
        self.cells = [(0, (0,0), 0)]

        self.is_growing = False
    def __repr__(self):
        return f'<Tree cords = {self.position}, is_growing = {self.is_growing}>'
class DNA:
    def __init__(self, code = None):
        if code is None:
            code = DNA.generate_code()
        self.code = code
    def get_specific_gen(self, num):
        return self.code[num]
    def division(self):
        if rnd.randint(0, 100) > settings.mutation_chance:
            return self.code
        mutated_gen_index = rnd.randint(0, settings.dna_code_rows - 1)
        mutated_gen = list(self.get_specific_gen(mutated_gen_index))
        mutated_gen[rnd.randint(0, settings.dna_row_symbols - 1)] = rnd.randint(0, settings.dna_max_symobl)
        code = list(self.code)
        code[mutated_gen_index] = tuple(mutated_gen)
        return tuple(code)
    @classmethod
    def generate_code(cls):
        code = tuple([tuple([rnd.randint(0, settings.dna_max_symobl) for z in range(settings.dna_row_symbols)]) for i in range(settings.dna_code_rows)])
        return code

class Map:
    def __init__(self, max_x = None, max_y = None):
        if max_x is None:
            max_x = settings.area_max_x
        if max_y is None:
            max_y = settings.area_max_y

        self.max_x = max_x
        self.max_y = max_y
        self.area = [[0 for z in range(max_x)] for i in range(max_y)]
        self.trees = [Tree(Map.get_random_area_cords(self.max_x, self.max_y))]

    def tick(self):
        for t in self.trees:
            if not t.is_growing:
                ac = self.get_around_cells(t.position[0], t.position[1])
                if t.position[0] < self.max_x:
                    print(ac)
                    if ac[2] == 0:
                        t.position = (t.position[0], t.position[1] + 1)
                else:
                    t.is_growing = True
    def get_specific_area(self, min_x, max_x, min_y, max_y):
        specific_area = []
        for row in self.area[min_y:max_y]:
            specific_area.append(row[min_x:max_x])
        return specific_area
    def get_specific_cell(self, x, y):
        return self.area[y - 1][x - 1]
    def get_around_cells(self, x, y):
        if x < self.max_x and y < self.max_y:
            return (self.area[x][y - 1], self.area[x - 1][y], self.area[x][y + 1], self.area[x + 1][y])
        return None
    @classmethod
    def get_random_area_cords(cls, max_x, max_y):
        return (rnd.randint(0, max_x), rnd.randint(0, max_y))


if __name__ == '__main__':
    t = Tree((1, 1))
    map = Map()
    for i in range(50):
        map.tick()
        print(map.trees)
    print(map.get_specific_cell(50, 40))
