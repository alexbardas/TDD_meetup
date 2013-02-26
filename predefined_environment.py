# This is how the world is defined
# Pacman starts from a5, has a S-like trajectory and when he reaches i1, he
#return on the exact same road. When he reaches a5 again, he will return again
# The ghost starts from i1 and has a O-like, circular trajectory
world = [
	['a1', 'a2', 'a3', 'a4', 'a5'],
	['b1', '', '', '', 'b5'],
	['c1', '', '', '', 'c5'],
	['d1', '', '', '', 'd5'],
	['e1', 'e2', 'e3', 'e4', 'e5'],
	['f1', '', '', '', 'f5'],
	['g1', '', '', '', 'g5'],
	['h1', '', '', '', 'h5'],
	['i1', 'i2', 'i3', 'i4', 'i5']
]

# The set of next allowed transitions from
transitions = {
	'pacman': ['a5', 'a4', 'a3', 'a2', 'a1', 'b1', 'c1', 'd1', 'e1', 'e2', 'e3',
				'e4', 'e5', 'f5','g5', 'h5', 'i5', 'i4', 'i3', 'i2', 'i1',],
	'ghost': ['i1', 'i2', 'i3', 'i4', 'i5', 'h5', 'g5', 'f5', 'e5', 'd5', 'c5',
			'b5', 'a5', 'a4', 'a3', 'a2', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1',
			'g1', 'h1', 'i1',]
}
# The list of neighbours, exactly how they are defined in the specs

neighbours = {
	'a1': ['b1', 'a2'],
	'a2': ['a1', 'a3'],
	'a3': ['a2', 'a4'],
	'a4': ['a3', 'a5'],
	'a5': ['a4', 'b5'],
	'b5': ['a5', 'c5'],
	'c5': ['b5', 'd5'],
	'd5': ['c5', 'e5'],
	'e5': ['d5', 'e4', 'f5'],
	'f5': ['e5', 'g5'],
	'g5': ['f5', 'h5'],
	'h5': ['g5', 'i5'],
	'b1': ['a1', 'c1'],
	'c1': ['b1', 'd1'],
	'd1': ['c1', 'e1'],
	'e1': ['d1', 'e2', 'f1'],
	'f1': ['e1', 'g1'],
	'g1': ['f1', 'h1'],
	'h1': ['g1', 'i1'],
	'i1': ['h1', 'i2'],
	'i2': ['i1', 'i3'],
	'i3': ['i2', 'i4'],
	'i4': ['i3', 'i5'],
	'i5': ['i4', 'h5'],
	'e2': ['e1', 'e3'],
	'e3': ['e2', 'e4'],
	'e4': ['e3', 'e5']
}