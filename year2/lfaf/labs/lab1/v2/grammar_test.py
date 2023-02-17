import unittest
from grammar import Grammar


class TestGrammar(unittest.TestCase):
    def setUp(self):
        non_terminals = {'S', 'D', 'R'}
        terminals = {'a', 'b', 'c', 'd', 'f'}
        productions = {
            'S': ['aS', 'bD', 'fR'],
            'D': ['cD', 'dR', 'd'],
            'R': ['bR', 'f']
        }
        start_symbol = 'S'
        self.grammar = Grammar(non_terminals, terminals, productions, start_symbol)

    def test_generate_strings(self):
        # Test that 5 strings are generated for n=5
        n = 5
        generated_strings = self.grammar.generate_strings(n)
        self.assertEqual(len(generated_strings), n)

        # Test that 0 strings are generated for n=0
        n = 0
        generated_strings = self.grammar.generate_strings(n)
        self.assertEqual(len(generated_strings), n)

        # Test that 10 strings are generated for n=10
        n = 10
        generated_strings = self.grammar.generate_strings(n)
        self.assertEqual(len(generated_strings), n)

    def test_invalid_nonterminal(self):
        # Test that a ValueError is raised for an invalid non-terminal symbol
        with self.assertRaises(ValueError):
            self.grammar.generate_strings_helper('X', '', 5, set())

    def test_invalid_n(self):
        # Test that a ValueError is raised for an invalid n value
        with self.assertRaises(ValueError):
            self.grammar.generate_strings(100)

    def test_productions_with_invalid_symbols(self):
        # Test that a ValueError is raised for productions containing invalid symbols
        productions = {
            'S': ['aS', 'bD', 'fR', 'X'],
            'D': ['cD', 'dR', 'd'],
            'R': ['bR', 'f']
        }
        with self.assertRaises(ValueError):
            Grammar({'S', 'D', 'R'}, {'a', 'b', 'c', 'd', 'f'}, productions, 'S')

    def test_productions_with_invalid_nonterminals(self):
        # Test that a ValueError is raised for productions containing invalid non-terminals
        productions = {
            'S': ['aS', 'bD', 'fR'],
            'D': ['cD', 'dR', 'd'],
            'R': ['bR', 'f'],
            'X': ['a']
        }
        with self.assertRaises(ValueError):
            Grammar({'S', 'D', 'R'}, {'a', 'b', 'c', 'd', 'f'}, productions, 'S')


if __name__ == '__main__':
    unittest.main()
