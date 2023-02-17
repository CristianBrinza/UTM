import unittest
from finite_automaton import FiniteAutomaton


class TestFiniteAutomaton(unittest.TestCase):
    def setUp(self):
        # Define a simple finite automaton for testing
        self.states = {'q0', 'q1'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q1',
            ('q1', '1'): 'q0'
        }
        self.start_state = 'q0'
        self.accept_states = {'q1'}
        self.fa = FiniteAutomaton(
            self.states,
            self.alphabet,
            self.transitions,
            self.start_state,
            self.accept_states
        )

    def test_accepts(self):
        # Test if the finite automaton correctly accepts/rejects input strings
        self.assertTrue(self.fa.accepts('110'))
        self.assertFalse(self.fa.accepts('1110'))
        self.assertFalse(self.fa.accepts(''))
        self.assertFalse(self.fa.accepts('10'))
        self.assertFalse(self.fa.accepts('1101'))

    def test_get_next_state(self):
        # Test if the finite automaton correctly transitions between states
        self.assertEqual(self.fa.get_next_state('q0', '0'), 'q0')
        self.assertEqual(self.fa.get_next_state('q0', '1'), 'q1')
        self.assertEqual(self.fa.get_next_state('q1', '0'), 'q1')
        self.assertEqual(self.fa.get_next_state('q1', '1'), 'q0')
        self.assertRaises(ValueError, self.fa.get_next_state, 'q2', '0')
        self.assertRaises(ValueError, self.fa.get_next_state, 'q1', '2')

    def test_add_transition(self):
        # Test if adding a transition modifies the finite automaton correctly
        self.fa.add_transition('q1', '0', 'q0')
        self.assertEqual(self.fa.get_next_state('q1', '0'), 'q0')
        self.assertEqual(self.fa.get_next_state('q1', '1'), 'q0')

    def test_remove_transition(self):
        # Test if removing a transition modifies the finite automaton correctly
        self.fa.remove_transition('q0', '1')
        self.assertEqual(self.fa.get_next_state('q0', '1'), None)

    def test_add_state(self):
        # Test if adding a state modifies the finite automaton correctly
        self.fa.add_state('q2')
        self.states.add('q2')
        self.assertEqual(self.fa.states, self.states)

    def test_remove_state(self):
        # Test if removing a state modifies the finite automaton correctly
        self.fa.remove_state('q1')
        self.states.remove('q1')
        self.assertEqual(self.fa.states, self.states)
        self.assertFalse('q1' in self.fa.accept_states)


if __name__ == '__main__':
    unittest.main()
