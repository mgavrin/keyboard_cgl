import sets
from game_of_life import board
import unittest

class TestBoardFunctions(unittest.TestCase):

    def test_exclude_neighbors(self):
        test_board = board()
        neighbors = sets.Set([(-1, -1), (-1, 0), (0, -1), (0, 0), (3,3),
                              (20, 5), (5, 20), (21, 5), (20, 6)])
        allowed_neighbors = test_board.exclude_out_of_bounds_neighbors(neighbors)
        expected = sets.Set([(0, 0), (3,3), (20, 5)])
        self.assertEqual(allowed_neighbors, expected)
        
    def test_exclue_neighbors_wraparound(self):
        #nothing should be excluded when wrap_around is true
        test_board = board(True)
        neighbors = sets.Set([(-1, -1), (-1, 0), (0, -1), (0, 0), (3,3),
                              (20, 5), (5, 20), (21, 5), (20, 6)])
        allowed_neighbors = test_board.exclude_out_of_bounds_neighbors(neighbors)
        expected = sets.Set([(0, 0), (3,3), (20, 5)])
        self.assertEqual(allowed_neighbors, expected)

    def test_update_dead_no_neighbors(self):
        test_board = board(True)
        self.assertEqual(test_board.update_cell(3,3), False)

    def test_update_dead_one_neighbor(self):
        pass

    def test_update_dead_two_neighbors(self):
        pass

    def test_update_dead_three_neighbors(self):
        pass

    def test_update_dead_four_neighbors(self):
        pass

    def test_update_alive_no_neighbors(self):
        pass

    def test_update_alive_one_neighbor(self):
        pass

    def test_update_alive_two_neighbors(self):
        pass

    def test_update_alive_three_neighbors(self):
        pass

    def test_update_alive_four_neighbors(self):
        pass

    

if __name__ == '__main__':
    unittest.main()
