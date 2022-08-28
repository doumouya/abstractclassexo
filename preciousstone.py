import gc

class PreciousStone:
    all_stones = []
    def __init__(self, stone):
        self.stone = stone
        self.add_stone(self)
    
    @classmethod
    def add_stone(cls, self):
        if len(cls.all_stones) == 5:
            del cls.all_stones[0]
            cls.all_stones.append(self)
        else:
            cls.all_stones.append(self)

stone1 = PreciousStone('Ruby')
stone1 = PreciousStone('Azurite')
stone1 = PreciousStone('Opal')
stone1 = PreciousStone('Turquoise')
stone1 = PreciousStone('Coral')

print('After adding 5 first stones')
for stone in PreciousStone.all_stones:
    print(stone.stone)

print('\n')
# print(PreciousStone.all_stones)

stone1 = PreciousStone('Dolomite')

print('After adding one last stone:')
for stone in PreciousStone.all_stones:
    print(stone.stone)
# print(PreciousStone.all_stones)

print('\n')

print('Checking total instances with garbage collector import:')
for obj in gc.get_objects():
    if isinstance(obj, PreciousStone):
        print(obj.stone)