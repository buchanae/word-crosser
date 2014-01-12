from collections import defaultdict, namedtuple


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        return Position(self.x - 1, self.y)
        
    def right(self):
        return Position(self.x + 1, self.y)

    def up(self):
        return Position(self.x, self.y - 1)

    def down(self):
        return Position(self.x, self.y + 1)

    @property
    def _key(self):
        return self.x, self.y

    def __eq__(self, other):
        return self._key == other._key

    def __hash__(self):
        return hash(self._key)

    def __repr__(self):
        return 'Position({}, {})'.format(self.x, self.y)


class Block(object): pass


class CellModificationError(Exception): pass

Cell = namedtuple('Cell', 'position content')


class Board(object):
    def __init__(self):
        self.cells = {}

    def __getitem__(self, key):
        return self.cells[key]

    def place_word(self, pos, word):
        self.set_block(pos.left())

        for letter in word:
            self.set_cell(pos, letter)
            pos = pos.right()

        self.set_block(pos)

    def set_cell(self, pos, content):
        if not isinstance(pos, Position):
            raise ValueError('set_cell() requires a Position')

        try:
            existing = self.cells[pos]
            if existing != content:
                raise CellModificationError()

        except KeyError:
            self.cells[pos] = content

    def set_block(self, pos):
        self.set_cell(pos, Block)

    def cols(self):
        cols = defaultdict(list)
        for pos, content in self.cells.items():
            cell = Cell(pos, content)
            cols[pos.x].append(cell)

        ret = []
        for x in self.xrange():
            col = sorted(cols[x], key=lambda cell: cell.position.y)
            ret.append((x, col))
            
        return ret

    def xrange(self):
        min_x = 0
        max_x = 0

        for key in self.cells:
            if key.x < min_x:
                min_x = key.x
            if key.x > max_x:
                max_x = key.x

        return range(min_x, max_x + 1)
