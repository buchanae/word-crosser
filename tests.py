import unittest

import board


class PositionTestCase(unittest.TestCase):
    def test_eq(self):
        a = board.Position(0, 0)
        b = board.Position(0, 0)
        c = board.Position(0, 1)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_hash(self):
        a = board.Position(0, 0)
        d = {}
        d[a] = 'foo'
        self.assertEqual(d[a], 'foo')

    def test_left(self):
        a = board.Position(0, 0)
        b = a.left()
        self.assertEqual(b.x, -1)
        self.assertEqual(b.y, 0)

    def test_right(self):
        a = board.Position(0, 0)
        b = a.right()
        self.assertEqual(b.x, 1)
        self.assertEqual(b.y, 0)

    def test_up(self):
        a = board.Position(0, 0)
        b = a.up()
        self.assertEqual(b.x, 0)
        self.assertEqual(b.y, -1)

    def test_down(self):
        a = board.Position(0, 0)
        b = a.down()
        self.assertEqual(b.x, 0)
        self.assertEqual(b.y, 1)
        
        
class BoardTestCase(unittest.TestCase):
    def test_set_cell(self):
        b = board.Board()
        p = board.Position(0, 0)
        b.set_cell(p, 'a')
        self.assertEqual(b.cells[p], 'a')

    def test_set_cell_modification_error(self):
        b = board.Board()
        p = board.Position(0, 0)
        b.set_cell(p, 'a')

        with self.assertRaises(board.CellModificationError):
            b.set_cell(p, 'b')

    def test_set_block(self):
        b = board.Board()
        p = board.Position(0, 0)
        b.set_block(p)
        self.assertEqual(b.cells[p], board.Block)

    def test_bad_position(self):
        b = board.Board()
        with self.assertRaises(ValueError):
            b.set_cell('foo', 'b')
        
    def test_place_word(self):
        b = board.Board()
        p = board.Position(0, 0)
        b.place_word(p, 'word')
        self.assertEqual(b[p], 'w')

        p = board.Position(1, 0)
        self.assertEqual(b[p], 'o')

        p = board.Position(2, 0)
        self.assertEqual(b[p], 'r')

        p = board.Position(3, 0)
        self.assertEqual(b[p], 'd')

        p = board.Position(-1, 0)
        self.assertEqual(b[p], board.Block)

        p = board.Position(4, 0)
        self.assertEqual(b[p], board.Block)

    def test_xrange(self):
        b = board.Board()
        self.assertEqual(b.xrange(), [0])

        p = board.Position(-10, 0)
        b.set_cell(p, 'a')

        self.assertEqual(b.xrange(), range(-10, 1))

        p = board.Position(10, 0)
        b.set_cell(p, 'a')

        self.assertEqual(b.xrange(), range(-10, 11))

    def test_columns(self):
        b = board.Board()
        p = board.Position(0, 0)
        b.place_word(p, 'word')
        self.assertEqual(b.cols(), [])


if __name__ == '__main__':
    unittest.main()
