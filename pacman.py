import copy
import os
import time
from predefined_environment import transitions, neighbours, world

pacman_positions = transitions['pacman']
ghost_positions = transitions['ghost']

# Given a position and a direction, return the new pacman's position
pacman_next = lambda position, direction: position + 1 if direction else position - 1

# The state the system has at clock == 0
initial_state = {
	'interval': 7,
	'clock': 0,
	'pacman': 0,
	'ghost': 0,
	'pacman_direction': False,
	'game_over': False,
	'pellets': [],
	'score': 0,
	'pacman_position': pacman_positions[0],
	'ghost_position': ghost_positions[0],
}

def on_clock(old_state):
	""" Given a state, in returns the state corresponding to the new clock tick
		@param {dict} old_state: a dict containing the current state
	"""
	# Make a deep copy of the old_state, to avoid mutating it
	state = copy.copy(old_state)

	# Increase clock time
	state['clock'] += 1

	# Determine the new pacman direction. It changes when it reaches an end
	if state['pacman'] == len(pacman_positions) - 1 or state['pacman'] == 0:
		state['pacman_direction'] = not state['pacman_direction']

	# Move the pacman on the next position
	state['pacman'] = pacman_next(state['pacman'], state['pacman_direction'])

	# Move the ghost on the next mosition
	state['ghost'] = (state['ghost'] + 1) % len(ghost_positions)

	# The state of pacman/ghost represents the index they currently have
	# in their position array. We also need to have a shortcut, representing
	# their position name (i.e.: a4, i7)
	pacman_position = pacman_positions[state['pacman']]
	ghost_position = ghost_positions[state['ghost']]

	# Given the current clock tick, determine if the ghost is poisonous or not
	ghost_is_deadly = False
	if state['clock'] % state['interval'] == 0:
		ghost_is_deadly = True
		# Every time the ghost is deadly, it drops a pellet. Save its position
		# in the state
		state['pellets'].append(ghost_position)

	# If pacman is on a position with a pellet, then retrieve the pellet and
	# increase the score
	if pacman_position in state['pellets']:
		state['pellets'].remove(pacman_position)
		state['score'] += 1

	# Pacman and ghost are on the same position and ghost is deadly
	if ghost_is_deadly and (
			pacman_position == ghost_position or
			pacman_position in neighbours[ghost_position] or
			ghost_position in neighbours[pacman_position]):

		state['game_over'] = True

	# Update pacman_position & ghost_position properties
	state.update({
		'pacman_position': pacman_position,
		'ghost_position': ghost_position,
		})

	return state

def _get_state(pos, state):
	""" String representation of the state in a given position
	@param {Char} pos
	@param {dict} state
	"""

	if pos == state['ghost_position'] and \
		state['clock'] % state['interval'] == 0:
		return ' ' + u'\u2620'.format(u'')
	elif pos == state['pacman_position'] and \
		pos == state['ghost_position']:
		return 'GP'
	elif pos == state['pacman_position']:
		return ' P'
	elif pos == state['ghost_position']:
		return ' G'
	elif pos in state['pellets']:
		return ' o'
	elif bool(pos):
		return ' .'
	else:
		return '  '
	return s

def show_world():
	state = copy.copy(initial_state)
	while True:
		os.system('clear')
		for line_idx, line in enumerate(world):
			s = ''
			for col_idx, col in enumerate(world[line_idx]):
				s += _get_state(world[line_idx][col_idx], state)
			print s
		print ''
		print 'Score %s' % state['score']
		print 'Tick %s' % state['clock']

		if state['game_over']:
			break

		state = on_clock(state)
		time.sleep(0.4)

if __name__ == '__main__':
    show_world()