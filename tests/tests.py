import unittest
import minesweeper


class ClassName(unittest.TestCase):
    def setUp(self):
        self.app = minesweeper.app.test_client()

    def test_grid_creator(self):
        grid = minesweeper.generate_grid()
        count = sum([len(col) for col in grid.values()])
        dedupCount = sum([len(set(col)) for col in grid.values()])
        self.assertEqual(99, count)
        self.assertEqual(count, dedupCount)

    def test_mine_hit(self):
        grid = {0: [0, 2],
                1: [1, 4]}
        self.assertEqual(True, minesweeper.find_mines(grid, 0, 0))
        self.assertEqual(True, minesweeper.find_mines(grid, 0, 2))
        self.assertEqual(True, minesweeper.find_mines(grid, 1, 1))
        self.assertEqual(True, minesweeper.find_mines(grid, 1, 4))

    def test_count(self):
        grid = {0: [0, 2]}
        grid2 = {0: [0, 2],
                 1: [1, 2]}
        self.assertEqual(2, minesweeper.find_mines(grid, 0, 1))
        self.assertEqual(4, minesweeper.find_mines(grid2, 0, 1))

    def test_endpoint(self):
        response = self.app.get("/1/2")
        print response.data