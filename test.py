import unittest
from pacman import on_clock, pacman_positions, ghost_positions

class Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_game_ends(self):
		state = {
			'interval': 5,
			'clock': 0,
			'pacman': 0,
			'ghost': 0,
			'pacman_direction': False,
			'pellets': [],
			'score': 0,
			'game_over': False,
		}

		state = on_clock(state)
		self.assertEqual(state['clock'], 1)
		self.assertEqual(state['pacman_position'], 'a4')
		self.assertEqual(state['ghost_position'], 'i2')
		self.assertFalse(state['game_over'])
		self.assertEqual(state['pellets'], [])
		self.assertEqual(state['score'], 0)


	def test_take_pellet(self):
		state = {
			'interval': 5,
			'clock': 0,
			'pacman': pacman_positions.index('d1'),
			'ghost': 0,
			'pacman_direction': True,
			'pellets': ['e1'],
			'score': 0,
			'game_over': False
		}

		state = on_clock(state)
		self.assertEqual(state['score'], 1)
		self.assertEqual(state['pellets'], [])

		state = on_clock(state)
		self.assertEqual(state['score'], 1)

		state = {
			'interval': 5,
			'clock': 0,
			'pacman': pacman_positions.index('e3'),
			'ghost': 0,
			'pacman_direction': False,
			'pellets': ['e1'],
			'score': 4,
			'game_over': False
		}

		state = on_clock(state)
		self.assertEqual(state['score'], 4)
		self.assertEqual(state['pellets'], ['e1'])

		state = on_clock(state)
		self.assertEqual(state['score'], 5)
		self.assertEqual(state['pellets'], [])

	def test_game_over(self):
		state = {
			'interval': 5,
			'clock': 4,
			'pacman': pacman_positions.index('f5'),
			'ghost': ghost_positions.index('h5'),
			'pacman_direction': True,
			'pellets': ['e1'],
			'score': 0,
			'game_over': False,
		}

		state = on_clock(state)
		self.assertTrue(state['game_over'])

	def test_change_direction(self):
		state = {
			'interval': 5,
			'clock': 4,
			'pacman': pacman_positions.index('i2'),
			'ghost': ghost_positions.index('f5'),
			'pacman_direction': True,
			'pellets': [],
			'score': 0,
			'game_over': False,
		}

		state = on_clock(state)
		self.assertEquals(state['pacman_direction'], True)
		self.assertEquals(state['pacman_position'], 'i1')

		state = on_clock(state)
		self.assertEquals(state['pacman_direction'], False)
		self.assertEquals(state['pacman_position'], 'i2')

		state = on_clock(state)
		self.assertEquals(state['pacman_direction'], False)

		state = {
			'interval': 5,
			'clock': 4,
			'pacman': pacman_positions.index('a4'),
			'ghost': ghost_positions.index('f5'),
			'pacman_direction': False,
			'pellets': [],
			'score': 0,
			'game_over': False,
		}

		state = on_clock(state)
		self.assertEquals(state['pacman_direction'], False)
		self.assertEquals(state['pacman_position'], 'a5')

		state = on_clock(state)
		self.assertEquals(state['pacman_direction'], True)
		self.assertEquals(state['pacman_position'], 'a4')


if __name__ == '__main__':
    unittest.main()